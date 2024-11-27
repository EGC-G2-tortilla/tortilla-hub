import logging
import os
import json
import requests
import shutil
import tempfile
import uuid
from datetime import datetime, timezone
from zipfile import ZipFile
from flamapy.metamodels.fm_metamodel.transformations import (
    UVLReader,
    GlencoeWriter,
    SPLOTWriter,
)
from flamapy.metamodels.pysat_metamodel.transformations import FmToPysat, DimacsWriter

from flask import (
    redirect,
    render_template,
    request,
    jsonify,
    send_from_directory,
    make_response,
    abort,
    url_for,
    send_file,
    session,
)
from flask_login import login_required, current_user

from app.modules.dataset.forms import DataSetForm
from app.modules.dataset.models import (
    DSDownloadRecord,
    DataSet,
    PublicationType,
)
from app.modules.dataset import dataset_bp
from app.modules.dataset.seeders import BaseSeeder
from app.modules.dataset.services import (
    AuthorService,
    DSDownloadRecordService,
    DSMetaDataService,
    DSViewRecordService,
    DataSetService,
    DOIMappingService,
)
from app.modules.fakenodo.services import FakenodoService
from app.modules.featuremodel.models import FMMetaData, FeatureModel
from app.modules.hubfile.models import Hubfile
from app.modules.hubfile.services import HubfileService
from app.modules.auth.models import OAuthProvider

logger = logging.getLogger(__name__)


dataset_service = DataSetService()
author_service = AuthorService()
dsmetadata_service = DSMetaDataService()
fakenodo_service = FakenodoService()
doi_mapping_service = DOIMappingService()
ds_view_record_service = DSViewRecordService()


@dataset_bp.route("/dataset/upload", methods=["GET", "POST"])
@login_required
def create_dataset():
    form = DataSetForm()
    if request.method == "POST":

        dataset = None

        if not form.validate_on_submit():
            return jsonify({"message": form.errors}), 400

        try:
            logger.info("Creating dataset...")
            dataset = dataset_service.create_from_form(
                form=form, current_user=current_user
            )
            logger.info(f"Created dataset: {dataset}")
            dataset_service.move_feature_models(dataset)
        except Exception as exc:
            logger.exception(f"Exception while create dataset data in local {exc}")
            return (
                jsonify({"Exception while create dataset data in local: ": str(exc)}),
                400,
            )

        # send dataset as deposition to Zenodo
        data = {}
        try:
            fakenodo_response_json = fakenodo_service.create_new_deposition(dataset)
            response_data = json.dumps(fakenodo_response_json)
            data = json.loads(response_data)
        except Exception as exc:
            data = {}
            fakenodo_response_json = {}
            logger.exception(f"Exception while create dataset data in Zenodo {exc}")

        if data.get("conceptrecid"):
            deposition_id = data.get("id")

            # update dataset with deposition id in Zenodo
            dataset_service.update_dsmetadata(
                dataset.ds_meta_data_id, deposition_id=deposition_id
            )

            try:
                # iterate for each feature model (one feature model = one request to Zenodo)
                for feature_model in dataset.feature_models:
                    fakenodo_service.upload_file(dataset, deposition_id, feature_model)

                # publish deposition
                fakenodo_service.publish_deposition(deposition_id)

                # update DOI
                deposition_doi = fakenodo_service.get_doi(deposition_id)
                dataset_service.update_dsmetadata(
                    dataset.ds_meta_data_id, dataset_doi=deposition_doi
                )
            except Exception as e:
                msg = f"it has not been possible upload feature models in Zenodo and update the DOI: {e}"
                return jsonify({"message": msg}), 200

        # Delete temp folder
        file_path = current_user.temp_folder()
        if os.path.exists(file_path) and os.path.isdir(file_path):
            shutil.rmtree(file_path)

        msg = "Everything works!"
        return jsonify({"message": msg}), 200

    return render_template("dataset/upload_dataset.html", form=form)


@dataset_bp.route("/dataset/list", methods=["GET", "POST"])
@login_required
def list_dataset():
    return render_template(
        "dataset/list_datasets.html",
        datasets=dataset_service.get_synchronized(current_user.id),
        local_datasets=dataset_service.get_unsynchronized(current_user.id),
    )


@dataset_bp.route("/dataset/file/upload", methods=["POST"])
@login_required
def upload():
    file = request.files["file"]
    temp_folder = current_user.temp_folder()

    if not file or not file.filename.endswith(".uvl"):
        return jsonify({"message": "No valid file"}), 400

    # create temp folder
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    file_path = os.path.join(temp_folder, file.filename)

    if os.path.exists(file_path):
        # Generate unique filename (by recursion)
        base_name, extension = os.path.splitext(file.filename)
        i = 1
        while os.path.exists(
            os.path.join(temp_folder, f"{base_name} ({i}){extension}")
        ):
            i += 1
        new_filename = f"{base_name} ({i}){extension}"
        file_path = os.path.join(temp_folder, new_filename)
    else:
        new_filename = file.filename

    try:
        # Guardar archivo
        file.save(file_path)

        # Validación de sintaxis del UVL utilizando el endpoint de validación
        with open(file_path, "rb") as f:
            validation_response = requests.post(
                url_for("flamapy.validate_uvl_file", _external=True),
                files={"file": f},
                timeout=20,
            )
        validation_data = validation_response.json()

        if validation_response.status_code != 200:
            os.remove(file_path)  # Eliminar archivo en caso de error
            return jsonify({"errors": validation_data["errors"]}), 400

        return (
            jsonify(
                {
                    "message": "UVL uploaded and validated successfully",
                    "filename": new_filename,
                }
            ),
            200,
        )

    except Exception as e:
        return jsonify({"message": str(e)}), 500


@dataset_bp.route("/dataset/file/delete", methods=["POST"])
def delete():
    data = request.get_json()
    filename = data.get("file")
    temp_folder = current_user.temp_folder()
    filepath = os.path.join(temp_folder, filename)

    if os.path.exists(filepath):
        os.remove(filepath)
        return jsonify({"message": "File deleted successfully"})

    return jsonify({"error": "Error: File not found"})


@dataset_bp.route("/dataset/download/<int:dataset_id>", methods=["GET"])
def download_dataset(dataset_id):
    dataset = dataset_service.get_or_404(dataset_id)

    file_path = f"uploads/user_{dataset.user_id}/dataset_{dataset.id}/"

    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, f"dataset_{dataset_id}.zip")

    with ZipFile(zip_path, "w") as zipf:
        for subdir, dirs, files in os.walk(file_path):
            for file in files:
                full_path = os.path.join(subdir, file)

                relative_path = os.path.relpath(full_path, file_path)

                zipf.write(
                    full_path,
                    arcname=os.path.join(
                        os.path.basename(zip_path[:-4]), relative_path
                    ),
                )

    user_cookie = request.cookies.get("download_cookie")
    if not user_cookie:
        user_cookie = str(
            uuid.uuid4()
        )  # Generate a new unique identifier if it does not exist
        # Save the cookie to the user's browser
        resp = make_response(
            send_from_directory(
                temp_dir,
                f"dataset_{dataset_id}.zip",
                as_attachment=True,
                mimetype="application/zip",
            )
        )
        resp.set_cookie("download_cookie", user_cookie)
    else:
        resp = send_from_directory(
            temp_dir,
            f"dataset_{dataset_id}.zip",
            as_attachment=True,
            mimetype="application/zip",
        )

    # Check if the download record already exists for this cookie
    existing_record = DSDownloadRecord.query.filter_by(
        user_id=current_user.id if current_user.is_authenticated else None,
        dataset_id=dataset_id,
        download_cookie=user_cookie,
    ).first()

    if not existing_record:
        # Record the download in your database
        DSDownloadRecordService().create(
            user_id=current_user.id if current_user.is_authenticated else None,
            dataset_id=dataset_id,
            download_date=datetime.now(timezone.utc),
            download_cookie=user_cookie,
        )

    return resp


@dataset_bp.route("/doi/<path:doi>/", methods=["GET"])
def subdomain_index(doi):

    # Check if the DOI is an old DOI
    new_doi = doi_mapping_service.get_new_doi(doi)
    if new_doi:
        # Redirect to the same path with the new DOI
        return redirect(url_for("dataset.subdomain_index", doi=new_doi), code=302)

    # Try to search the dataset by the provided DOI (which should already be the new one)
    ds_meta_data = dsmetadata_service.filter_by_doi(doi)

    if not ds_meta_data:
        abort(404)

    # Get dataset
    dataset = ds_meta_data.data_set
    # Check if the user id is also in the table o_auth_provider
    auth = False
    if current_user.is_authenticated:
        provider = OAuthProvider.query.filter_by(user_id=current_user.id).first()
        is_github = provider.provider_name == "github" if provider else False
        if is_github:
            auth = True

    # Save the cookie to the user's browser
    user_cookie = ds_view_record_service.create_cookie(dataset=dataset)
    resp = make_response(render_template("dataset/view_dataset.html", dataset=dataset, auth=auth))
    resp.set_cookie("view_cookie", user_cookie)

    return resp


@dataset_bp.route("/dataset/unsynchronized/<int:dataset_id>/", methods=["GET"])
@login_required
def get_unsynchronized_dataset(dataset_id):

    # Get dataset
    dataset = dataset_service.get_unsynchronized_dataset(current_user.id, dataset_id)

    if not dataset:
        abort(404)

    return render_template("dataset/view_dataset.html", dataset=dataset)


ZIP_FOLDER = os.path.join(os.getcwd(), "app", "modules", "dataset")


UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")


def set_full_permissions(directory):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            os.chmod(os.path.join(root, dir_name), 0o600)
        for file_name in files:
            os.chmod(os.path.join(root, file_name), 0o600)
    os.chmod(directory, 0o600)


@dataset_bp.route("/dataset/upload_zip/<int:dataset_id>", methods=["POST"])
def upload_from_zip(dataset_id):
    try:
        # Paso 1: Obtener el dataset y la carpeta temporal
        try:
            dataset = dataset_service.get_or_404(dataset_id)
            temp_folder = current_user.temp_folder()
            if not os.path.exists(temp_folder):
                os.makedirs(temp_folder)
            else:
                shutil.rmtree(
                    temp_folder
                )  # Limpia la carpeta temporal para evitar residuos
                os.makedirs(temp_folder)
        except Exception as e:
            logging.error(f"Error al preparar la carpeta temporal: {e}")
            return (
                jsonify(
                    {"message": f"Error al preparar la carpeta temporal: {str(e)}"}
                ),
                500,
            )

        # Paso 2: Validar y guardar el archivo ZIP
        try:
            file = request.files.get("zipFile")
            if not file or not file.filename.endswith(".zip"):
                return jsonify({"message": "No valid file"}), 400
            file_path = os.path.join(temp_folder, file.filename)
            file.save(file_path)
        except Exception as e:
            logging.error(f"Error al guardar el archivo ZIP: {e}")
            return (
                jsonify({"message": f"Error al guardar el archivo ZIP: {str(e)}"}),
                500,
            )

        # Paso 3: Extraer archivos del ZIP
        try:
            with ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(temp_folder)
                extracted_files = (
                    zip_ref.namelist()
                )  # Obtener la lista de archivos extraídos
        except Exception as e:
            logging.error(f"Error al extraer el archivo ZIP: {e}")
            return (
                jsonify({"message": f"Error al extraer el archivo ZIP: {str(e)}"}),
                500,
            )

        # Paso 4: Guardar en la carpeta uploads con nombres únicos
        try:
            upload_folder = os.path.join(
                UPLOAD_FOLDER, f"user_{dataset.user_id}/dataset_{dataset_id}/"
            )
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder, exist_ok=True)

            existing_files = set(os.listdir(upload_folder))
            renamed_files = []  # Para almacenar los nombres finales de los archivos

            for file in extracted_files:
                # Ignorar directorios
                if file.endswith("/"):
                    continue

                # Ruta completa del archivo extraído
                full_path = os.path.join(temp_folder, file)

                if os.path.isfile(full_path):
                    # Generar un nombre único si el archivo ya existe
                    base_name, extension = os.path.splitext(os.path.basename(file))
                    new_filename = base_name + extension
                    counter = 1

                    while new_filename in existing_files:
                        new_filename = f"{base_name}_{counter}{extension}"
                        counter += 1

                    # Mover el archivo al upload_folder con el nombre único
                    new_path = os.path.join(upload_folder, new_filename)
                    shutil.move(full_path, new_path)
                    renamed_files.append(new_filename)
                    existing_files.add(new_filename)

        except Exception as e:
            logging.error(f"Error al guardar archivos en uploads: {e}")
            return (
                jsonify({"message": f"Error al guardar archivos en uploads: {str(e)}"}),
                500,
            )

        # Paso 5: Mover los archivos renombrados a zip_files
        try:
            zip_files_folder = os.path.join(ZIP_FOLDER, "zip_files")
            if not os.path.exists(zip_files_folder):
                os.makedirs(zip_files_folder, exist_ok=True)

            for file in renamed_files:
                src_path = os.path.join(upload_folder, file)
                dest_path = os.path.join(zip_files_folder, file)

                shutil.copy(src_path, dest_path)  # Copiar a zip_files

        except Exception as e:
            logging.error(f"Error al mover archivos a zip_files: {e}")
            return (
                jsonify({"message": f"Error al mover archivos a zip_files: {str(e)}"}),
                500,
            )

        # Paso 6: Limpieza y confirmación
        folder = os.path.join(ZIP_FOLDER, "zip_files")
        add_files_to_dataset(dataset_id, folder)
        try:
            shutil.rmtree(temp_folder)
            return jsonify({"message": "Files uploaded successfully"}), 200
        except Exception as e:
            logging.error(f"Error al limpiar la carpeta temporal: {e}")
            return (
                jsonify({"message": f"Error al limpiar la carpeta temporal: {str(e)}"}),
                500,
            )

    except Exception as e:
        logging.error(f"Error inesperado en upload_from_zip: {e}")
        return jsonify({"message": f"Unexpected server error: {str(e)}"}), 500


def add_files_to_dataset(dataset_id, folder):
    files = [
        f
        for f in os.listdir(folder)
        if f.endswith(".uvl") and not f.startswith("._")
    ]

    for file in files:
        try:
            if not file.startswith("file") or not file.endswith(".uvl"):
                logging.error(f"Archivo con nombre inesperado: {file}")
                continue

            # Extraer índice del archivo
            i = int(file.split(".")[0][4:])

            # Crear metadatos
            fm_meta_data = FMMetaData(
                uvl_filename=f"file{i}.uvl",
                title=f"Feature Model {i}",
                description=f"Description for feature model {i}",
                # (Por defecto) Es necesario para gaurdar los modelos
                publication_type=PublicationType.SOFTWARE_DOCUMENTATION,
                publication_doi="",
                tags="",
                uvl_version="1.0",
            )
            try:
                seeder = BaseSeeder()
                seeder.seed([fm_meta_data])  # Pasar como lista
            except Exception as e:
                logging.error("Error procesando el archivo: %s", e)
                continue

            # Crear modelo de características
            feature_model = FeatureModel(
                data_set_id=dataset_id, fm_meta_data_id=fm_meta_data.id
            )
            seeder = BaseSeeder()
            seeder.seed([feature_model])  # Pasar como lista

            # Crear el archivo asociado
            file_path = os.path.join(folder, file)
            uvl_file = Hubfile(
                name=file,
                checksum=f"checksum{i}",
                size=os.path.getsize(file_path),
                feature_model_id=feature_model.id,
            )
            seeder = BaseSeeder()
            seeder.seed([uvl_file])  # Pasar como lista

            # add model to dataset
            dataset = DataSet.query.get(dataset_id)
            dataset.feature_models.append(feature_model)
            seeder.seed([dataset])

        except Exception as e:
            logging.error(f"Error procesando el archivo {file}: {e}")
            continue

    logging.info("Archivos procesados e insertados en la base de datos correctamente.")
    # eliminar la carpeta zip_files
    shutil.rmtree(folder)


@dataset_bp.route("/dataset/stage/<int:dataset_id>", methods=["GET"])
@login_required
def stage_dataset(dataset_id):
    dataset_service.set_dataset_to_staged(dataset_id)
    return render_template(
        "dataset/list_datasets.html",
        datasets=dataset_service.get_synchronized(current_user.id),
        local_datasets=dataset_service.get_unsynchronized(current_user.id),
    )


@dataset_bp.route("/dataset/unstage/<int:dataset_id>", methods=["GET"])
@login_required
def unstage_dataset(dataset_id):
    dataset_service.set_dataset_to_unstaged(dataset_id)
    return render_template(
        "dataset/list_datasets.html",
        datasets=dataset_service.get_synchronized(current_user.id),
        local_datasets=dataset_service.get_unsynchronized(current_user.id),
    )


@dataset_bp.route("/dataset/publish", methods=["GET"])
@login_required
def publish_datasets():
    dataset_service.publish_datasets(current_user_id=current_user.id)
    return render_template(
        "dataset/list_datasets.html",
        datasets=dataset_service.get_synchronized(current_user.id),
        local_datasets=dataset_service.get_unsynchronized(current_user.id),
    )


@dataset_bp.route("/dataset/stage/all", methods=["GET"])
@login_required
def stage_all_datasets():
    dataset_service.stage_all_datasets(current_user.id)
    return render_template(
        "dataset/list_datasets.html",
        datasets=dataset_service.get_synchronized(current_user.id),
        local_datasets=dataset_service.get_unsynchronized(current_user.id),
    )


def to_glencoe(file_id, full_path):
    try:
        # Obtener el archivo original usando el file_id
        hubfile = HubfileService().get_by_id(file_id)

        # Realizar las transformaciones necesarias
        fm = UVLReader(hubfile.get_path()).transform()

        # Generar el nombre final del archivo transformado
        final_file_name = f"{hubfile.name}_glencoe.txt"

        # Combinar el full_path (directorio) con el nombre final del archivo
        final_full_path = os.path.join(full_path, final_file_name)

        # Escribir el archivo transformado en la ruta completa final
        GlencoeWriter(final_full_path, fm).transform()

        # Devolver la ruta completa al archivo transformado
        return final_full_path
    except Exception as e:
        raise e


def to_splot(file_id, full_path):
    try:
        # Obtener el archivo original usando el file_id
        hubfile = HubfileService().get_by_id(file_id)

        # Realizar las transformaciones necesarias
        fm = UVLReader(hubfile.get_path()).transform()

        # Generar el nombre final del archivo transformado
        final_file_name = f"{hubfile.name}_splot.txt"

        # Combinar el full_path (directorio) con el nombre final del archivo
        final_full_path = os.path.join(full_path, final_file_name)

        # Escribir el archivo transformado en la ruta completa final
        SPLOTWriter(final_full_path, fm).transform()

        # Devolver la ruta completa al archivo transformado
        return final_full_path
    except Exception as e:
        raise e


def to_cnf(file_id, full_path):
    try:
        # Obtener el archivo original usando el file_id
        hubfile = HubfileService().get_by_id(file_id)

        # Realizar las transformaciones necesarias
        fm = UVLReader(hubfile.get_path()).transform()
        sat = FmToPysat(fm).transform()

        # Generar el nombre final del archivo transformado
        final_file_name = f"{hubfile.name}_cnf.txt"

        # Combinar el full_path (directorio) con el nombre final del archivo
        final_full_path = os.path.join(full_path, final_file_name)

        # Escribir el archivo transformado en la ruta completa final
        DimacsWriter(final_full_path, sat).transform()

        # Devolver la ruta completa al archivo transformado
        return final_full_path
    except Exception as e:
        raise e


@dataset_bp.route("/dataset/download_all", methods=["GET"])
def download_all_datasets():
    datasets = dataset_service.get_all_datasets()

    # Crear un directorio temporal para almacenar archivos originales y transformados
    temp_dir = tempfile.mkdtemp()
    original_dir = os.path.join(temp_dir, "original_files")
    transformed_dir = os.path.join(temp_dir, "transformed_files")
    os.makedirs(original_dir, exist_ok=True)
    os.makedirs(transformed_dir, exist_ok=True)

    zip_path = os.path.join(temp_dir, "all_datasets.zip")

    try:
        with ZipFile(zip_path, "w") as zipf:
            for dataset in datasets:
                file_path = f"uploads/user_{dataset.user_id}/dataset_{dataset.id}/"

                # Procesar archivos .uvl y sus transformaciones
                for subdir, dirs, files in os.walk(file_path):
                    for file in files:
                        full_path = os.path.join(subdir, file)
                        relative_path = os.path.relpath(full_path, file_path)

                        # Copiar archivos originales a la carpeta temporal y agregarlos al ZIP
                        original_file_path = os.path.join(original_dir, relative_path)
                        os.makedirs(os.path.dirname(original_file_path), exist_ok=True)
                        shutil.copy(full_path, original_file_path)
                        zipf.write(
                            original_file_path,
                            arcname=os.path.relpath(original_file_path, temp_dir),
                        )
                        logging.debug(
                            f"Archivo original agregado al ZIP: {relative_path}"
                        )

                        # Solo procesar archivos .uvl para las transformaciones
                        if file.endswith(".uvl"):
                            try:
                                # Obtener el file_id desde el nombre del archivo
                                file_id = int(file.split(".")[0][4:])
                            except ValueError:
                                logging.error(
                                    f"Error al extraer file_id del archivo: {file}"
                                )
                                continue  # Ignorar si no se puede extraer el ID correctamente

                            # Generar transformaciones en la carpeta temporal
                            try:
                                cnf_file = to_cnf(file_id, transformed_dir)
                                splot_file = to_splot(file_id, transformed_dir)
                                glencoe_file = to_glencoe(file_id, transformed_dir)

                                # Agregar transformaciones al ZIP
                                zipf.write(
                                    cnf_file,
                                    arcname=os.path.relpath(cnf_file, temp_dir),
                                )
                                zipf.write(
                                    splot_file,
                                    arcname=os.path.relpath(splot_file, temp_dir),
                                )
                                zipf.write(
                                    glencoe_file,
                                    arcname=os.path.relpath(glencoe_file, temp_dir),
                                )
                            except Exception as e:
                                logging.error(
                                    f"Error al transformar archivo {file}: {e}"
                                )
                                continue

        # Enviar el archivo ZIP para descarga
        return send_file(
            zip_path,
            as_attachment=True,
            mimetype="application/zip",
            download_name="all_datasets.zip",
        )
    finally:
        # Eliminar el directorio temporal después de su uso
        shutil.rmtree(temp_dir)


@dataset_bp.route("/dataset/download_repo_zip", methods=["POST"])
@login_required
def download_repo_zip():
    repo_url = request.form.get('repo_url')
    if not repo_url:
        return jsonify({"error": "No se proporcionó la URL del repositorio"}), 400

    # Validar y extraer el nombre del repositorio y el propietario de la URL
    if not repo_url.startswith("https://github.com/") or not repo_url.endswith(".git"):
        return jsonify({"error": "URL del repositorio no válida"}), 400

    parts = repo_url[len("https://github.com/"):-len(".git")].split('/')
    if len(parts) != 2:
        return jsonify({"error": "URL del repositorio no válida"}), 400

    owner, repo_name = parts

    branch = 'main'  # Puedes cambiar esto si necesitas una rama específica

    zip_url = f'https://github.com/{owner}/{repo_name}/archive/refs/heads/{branch}.zip'
    
    response = requests.get(zip_url)

    temp_folder = current_user.temp_folder()
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    zip_path = os.path.join(temp_folder, f'{repo_name}.zip')
    with open(zip_path, 'wb') as f:
        f.write(response.content)

    # Descomprimir el archivo ZIP
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_folder)

    # Encontrar todos los archivos .uvl
    uvl_files = []
    for root, dirs, files in os.walk(temp_folder):
        for file in files:
            if file.endswith('.uvl'):
                uvl_files.append(os.path.join(root, file))

    # Devolver la lista de archivos .uvl encontrados
    return jsonify(uvl_files)


@dataset_bp.route("/dataset/upload_github_files", methods=["POST"])
@login_required
def upload_from_github():
    dataset_id = request.form.get('dataset_id')
    selected_files = request.form.getlist('files')
    dataset = dataset_service.get_or_404(dataset_id)

    if not selected_files:
        return jsonify({"error": "No se seleccionaron archivos"}), 400

    temp_folder = current_user.temp_folder()
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    # Copiar los archivos seleccionados a la carpeta temporal
    for file_path in selected_files:
        if not os.path.exists(file_path):
            return jsonify({"error": f"El archivo {file_path} no existe"}), 400

        file_name = os.path.basename(file_path)
        dest_path = os.path.join(temp_folder, file_name)
        shutil.copy(file_path, dest_path)

    # Crear la carpeta del dataset si no existe
    try:
        upload_folder = os.path.join(
            UPLOAD_FOLDER, f"user_{dataset.user_id}/dataset_{dataset_id}/"
        )
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder, exist_ok=True)

        existing_files = set(os.listdir(upload_folder))
        renamed_files = []  # Para almacenar los nombres finales de los archivos

        for file in selected_files:
            # Ignorar directorios
            file_name = os.path.basename(file)
            if file_name.endswith("/"):
                continue

            # Ruta completa del archivo extraído
            full_path = os.path.join(temp_folder, file_name)
            print(full_path)

            if os.path.isfile(full_path):
                # Generar un nombre único si el archivo ya existe
                base_name, extension = os.path.splitext(os.path.basename(file))
                new_filename = base_name + extension
                counter = 1

                while new_filename in existing_files:
                    new_filename = f"{base_name}_{counter}{extension}"
                    counter += 1

                # Mover el archivo al upload_folder con el nombre único
                new_path = os.path.join(upload_folder, new_filename)
                shutil.copy(full_path, new_path)
                renamed_files.append(new_filename)
                existing_files.add(new_filename)

    except Exception as e:
        logging.error(f"Error al guardar archivos en uploads: {e}")
        return (
            jsonify({"message": f"Error al guardar archivos en uploads: {str(e)}"}),
            500,
        )
        
    # Añadir los archivos al dataset utilizando add_files_to_dataset
    add_files_to_dataset(dataset_id, temp_folder)

    return jsonify({"message": "Archivos subidos exitosamente"})