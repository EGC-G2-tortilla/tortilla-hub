import hashlib
import tempfile
import pytest
from app import db
from app.modules.featuremodel.models import FeatureModel
from app.modules.dataset.models import DSMetaData, PublicationType, DataSet


def calculate_checksum(file_content):
    """
    Calcula un checksum MD5 basado en el contenido del archivo.
    """
    return hashlib.md5(file_content.encode('utf-8')).hexdigest()


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extiende la configuración de `test_client` para añadir datos específicos de prueba.
    """
    with test_client.application.app_context():
        yield test_client


def create_temp_uvl_file(content):
    """
    Crea un archivo UVL temporal con el contenido proporcionado y devuelve la ruta.
    """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".uvl")
    with open(temp_file.name, "w") as file:
        file.write(content)
    return temp_file.name


def test_fm_fact_labels_empty_model(test_client):
    """
    Test negativo: Calcular etiquetas FM para un modelo vacío (sin features ni constraints).
    """
    with test_client.application.app_context():
        ds_meta_data = DSMetaData(
            title="Empty FM Dataset",
            description="Dataset with empty FM",
            publication_type=PublicationType.TECHNICAL_NOTE,
        )
        db.session.add(ds_meta_data)
        db.session.commit()

        dataset = DataSet(user_id=1, ds_meta_data_id=ds_meta_data.id)
        db.session.add(dataset)
        db.session.commit()

        feature_model = FeatureModel(data_set_id=dataset.id)
        db.session.add(feature_model)
        db.session.commit()

        response = feature_model.fact_labels

        assert response["number_of_features"] == 0, "Expected 0 features for empty model"
        assert response["constraints_count"] == 0, "Expected 0 constraints for empty model"
        assert response["max_depth"] == 0, "Expected 0 max depth for empty model"
        assert response["variability"] == 0.0, "Expected 0.0 variability for empty model"


def test_fm_fact_labels_empty_dataset(test_client):
    """
    Test negativo: Calcular fact labels para un dataset completamente vacío.
    """
    with test_client.application.app_context():
        ds_meta_data = DSMetaData(
            title="Empty Dataset",
            description="Empty dataset",
            publication_type=PublicationType.TECHNICAL_NOTE,
        )
        db.session.add(ds_meta_data)
        db.session.commit()

        dataset = DataSet(user_id=1, ds_meta_data_id=ds_meta_data.id)
        db.session.add(dataset)
        db.session.commit()

        feature_model = FeatureModel(data_set_id=dataset.id)
        db.session.add(feature_model)
        db.session.commit()

        response = feature_model.fact_labels

        assert response == {
            "number_of_features": 0,
            "constraints_count": 0,
            "max_depth": 0,
            "variability": 0.0,
        }, "Expected default fact labels for an empty dataset."
