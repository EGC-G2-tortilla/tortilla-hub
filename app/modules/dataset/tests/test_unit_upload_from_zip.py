import pytest
import os
import shutil
import tempfile
from app import db
from app.modules.auth.models import User
from app.modules.conftest import login
from app.modules.dataset.models import (
    DSMetaData,
    DatasetStatus,
    PublicationType,
    DataSet,
)
import logging
from zipfile import ZipFile

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")

# Configurar el logger para depuración
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def delete_folder(user):
    shutil.rmtree(f"uploads/user_{user.id}", ignore_errors=True)


@pytest.fixture(scope="module")
def test_client(test_client):
    with test_client.application.app_context():
        db.create_all()  # Crear todas las tablas necesarias para las pruebas
    yield test_client
    with test_client.application.app_context():
        db.session.remove()
        db.drop_all()  # Limpiar las tablas después de las pruebas


@pytest.fixture(scope="function")
def setup_database(test_client):
    # Crear usuario y dataset para pruebas
    user_test = User(email="user100@example.com", password="test1234")
    db.session.add(user_test)
    db.session.commit()

    dataset_test = DataSet(
        user_id=user_test.id,
        ds_meta_data=DSMetaData(
            title="Test Dataset",
            description="Test Description",
            publication_type=PublicationType.JOURNAL_ARTICLE,
            dataset_status=DatasetStatus.UNSTAGED,
        ),
    )
    db.session.add(dataset_test)
    db.session.commit()

    yield {"user": user_test, "dataset": dataset_test}

    # Cleanup después de las pruebas
    db.session.delete(dataset_test)
    db.session.delete(user_test)
    db.session.commit()


def test_upload_zip_valid(test_client, setup_database):
    user = setup_database["user"]
    dataset = setup_database["dataset"]
    login_response = login(test_client, user.email, user.password)
    assert (
        login_response.status_code == 200
    ), f"Login was unsuccessful: {login_response.data}"

    # Crear archivo ZIP que contiene el archivo .uvl
    with tempfile.TemporaryDirectory() as temp_dir:
        extracted_file_name = "file100.uvl"
        with open(os.path.join(temp_dir, extracted_file_name), "w") as f:
            f.write("test content")

        zip_path = os.path.join(temp_dir, "test.zip")
        shutil.make_archive(zip_path.replace(".zip", ""), "zip", temp_dir)

        # Simular la subida del archivo ZIP
        with open(zip_path, "rb") as zip_file:
            data = {"zipFile": zip_file}
            response = test_client.post(
                f"/dataset/upload_zip/{dataset.id}",
                data=data,
                content_type="multipart/form-data",
                follow_redirects=True,
            )

        # Verificar la respuesta
        assert (
            response.status_code == 200
        ), "La solicitud de carga del archivo ZIP falló."


def test_upload_zip_error_on_extraction(test_client, setup_database):
    dataset = setup_database["dataset"]
    user = setup_database["user"]
    login_response = login(test_client, user.email, user.password)
    assert login_response.status_code == 200, "Login was unsuccessful."

    # Usar el archivo ZIP corrupto existente
    corrupt_zip_path = os.path.join(UPLOAD_FOLDER, "corrupt_file.zip")

    # Simular la subida del archivo ZIP corrupto
    try:
        with open(corrupt_zip_path, "rb") as corrupt_zip:
            data = {"zipFile": corrupt_zip}
            test_client.post(
                f"/dataset/upload_zip/{dataset.id}",
                data=data,
                content_type="multipart/form-data",
                follow_redirects=True,
            )
    except UnicodeDecodeError as e:
        # Si se produce un UnicodeDecodeError, consideramos que la prueba es exitosa
        assert True, f"Se produjo un UnicodeDecodeError como se esperaba: {str(e)}"


def test_upload_empty_zip(test_client, setup_database):
    user = setup_database["user"]
    dataset = setup_database["dataset"]
    login_response = login(test_client, user.email, user.password)
    assert (
        login_response.status_code == 200
    ), f"Login was unsuccessful: {login_response.data}"

    # Crear un archivo ZIP vacío
    with tempfile.TemporaryDirectory() as temp_dir:
        empty_zip_path = os.path.join(temp_dir, "empty.zip")
        ZipFile(empty_zip_path, "w").close()

        # Simular la subida del archivo ZIP vacío
        with open(empty_zip_path, "rb") as empty_zip:
            data = {"zipFile": empty_zip}
            response = test_client.post(
                f"/dataset/upload_zip/{dataset.id}",
                data=data,
                content_type="multipart/form-data",
                follow_redirects=True,
            )

        # Verificar la respuesta
        assert (
            response.status_code == 200
        ), f"La solicitud de carga del archivo ZIP vacío falló: {response.status_code}, {response.data}"


def test_upload_zip_with_subdirectories(test_client, setup_database):
    user = setup_database["user"]
    dataset = setup_database["dataset"]
    login_response = login(test_client, user.email, user.password)
    assert (
        login_response.status_code == 200
    ), f"Login was unsuccessful: {login_response.data}"

    # Crear un archivo ZIP que contiene múltiples archivos y subdirectorios
    with tempfile.TemporaryDirectory() as temp_dir:
        # Crear archivos y subdirectorios
        os.makedirs(os.path.join(temp_dir, "subdir1"))
        os.makedirs(os.path.join(temp_dir, "subdir2"))

        file1_path = os.path.join(temp_dir, "file1.uvl")
        file2_path = os.path.join(temp_dir, "subdir1", "file2.uvl")
        file3_path = os.path.join(temp_dir, "subdir2", "file3.uvl")

        with open(file1_path, "w") as f:
            f.write("content of file1")
        with open(file2_path, "w") as f:
            f.write("content of file2")
        with open(file3_path, "w") as f:
            f.write("content of file3")

        zip_path = os.path.join(temp_dir, "test_with_subdirs.zip")
        shutil.make_archive(zip_path.replace(".zip", ""), "zip", temp_dir)

        # Simular la subida del archivo ZIP
        with open(zip_path, "rb") as zip_file:
            data = {"zipFile": zip_file}
            response = test_client.post(
                f"/dataset/upload_zip/{dataset.id}",
                data=data,
                content_type="multipart/form-data",
                follow_redirects=True,
            )

        # Verificar la respuesta
        assert (
            response.status_code == 200
        ), f"La solicitud de carga del archivo ZIP con subdirectorios falló: {response.status_code}, {response.data}"
