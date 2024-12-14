from app.modules.conftest import login, logout
from app import db
import pytest
from app.modules.auth.models import User
from app.modules.dataset.models import (
    DSMetaData,
    DatasetStatus,
    PublicationType,
    DataSet,
)


@pytest.fixture(scope="module")
def test_client(test_client):
    with test_client.application.app_context():
        db.create_all()  # Crear todas las tablas necesarias para las pruebas
    yield test_client
    with test_client.application.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="function")
def setup_database(test_client):
    # Crear usuario y dataset para pruebas
    user_test = User(email="user101@example.com", password="test1234")
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


def test_download_repo_zip_valid(test_client, setup_database):
    user = setup_database["user"]
    login_response = login(test_client, user.email, user.password)
    assert (
        login_response.status_code == 200
    ), f"Login was unsuccessful: {login_response.data}"

    # URL válida pero sin garantizar que la descarga funcione
    repo_url = "https://github.com/user/repo.git"
    response = test_client.post(
        "/dataset/download_repo_zip",
        data={"repo_url": repo_url},
        content_type="application/x-www-form-urlencoded",
        follow_redirects=True,
    )

    # Verificar respuesta
    assert (
        response.status_code == 200
    ), "La solicitud debería tener una respuesta válida"
    if response.status_code == 400:
        assert (
            "error" in response.json
        ), "Debe existir un mensaje de error en la respuesta"
    logout(test_client)


def test_upload_github_files_with_files(test_client, setup_database):
    user = setup_database["user"]
    dataset = setup_database["dataset"]
    login_response = login(test_client, user.email, user.password)
    assert (
        login_response.status_code == 200
    ), f"Login was unsuccessful: {login_response.data}"

    # Simular archivos seleccionados
    selected_files = ["/path/to/file1.uvl", "/path/to/file2.uvl"]
    response = test_client.post(
        "/dataset/upload_github_files",
        data={
            "dataset_id": dataset.id,
            "files": selected_files,
        },
        content_type="application/x-www-form-urlencoded",
        follow_redirects=True,
    )

    # Verificar respuesta
    assert response.status_code == 200, "Debería manejar correctamente la solicitud con archivos seleccionados"
    logout(test_client)
