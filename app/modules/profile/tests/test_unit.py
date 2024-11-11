import pytest

from app import db
from app.modules.conftest import login, logout
from app.modules.auth.models import User
from app.modules.profile.models import UserProfile
from app.modules.dataset.models import DSMetaData, PublicationType, DataSet

@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    for module testing (por example, new users)
    """
    with test_client.application.app_context():
        user_test = User(email='user@example.com', password='test1234')
        db.session.add(user_test)
        db.session.commit()

        profile = UserProfile(user_id=user_test.id, name="Name", surname="Surname")
        db.session.add(profile)
        db.session.commit()

    yield test_client


def test_edit_profile_page_get(test_client):
    """
    Tests access to the profile editing page via a GET request.
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/profile/edit")
    assert response.status_code == 200, "The profile editing page could not be accessed."
    assert b"Edit profile" in response.data, "The expected content is not present on the page"

    logout(test_client)


def test_view_other_user_profile(test_client):
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    other_user = User(email="other_user@example.com", password="password123")
    db.session.add(other_user)
    db.session.commit()

    other_profile = UserProfile(user_id=other_user.id, name="Other", surname="User")
    db.session.add(other_profile)
    db.session.commit()

    response = test_client.get(f"/profile/summary/{other_user.id}")
    assert response.status_code == 200, "Error accessing the other user's profile."


def test_view_other_user_profile_with_pagination(test_client):
    # Inicio de sesión del usuario de prueba
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    # Crear otro usuario y su perfil
    other_user = User(email="other_user2@example.com", password="password123")
    db.session.add(other_user)
    db.session.commit()

    other_profile = UserProfile(user_id=other_user.id, name="Empanada", surname="User")
    db.session.add(other_profile)
    db.session.commit()

    # Crear DSMetaData y DataSet asociados
    ds_meta_data = DSMetaData(
        title="Sample Dataset",
        description="Sample dataset description",
        publication_type=PublicationType.JOURNAL_ARTICLE,
    )
    db.session.add(ds_meta_data)
    db.session.commit()

    data_set = DataSet(
        user_id=other_user.id,
        ds_meta_data_id=ds_meta_data.id
    )
    db.session.add(data_set)
    db.session.commit()

    # Realizar la solicitud
    response = test_client.get(f'/profile/summary/{other_user.id}?page=1')
    assert response.status_code == 200

    # También puedes verificar la estructura HTML de la tarjeta de perfil
    assert b'<p class="card-text h5"><i class="fa fa-user"></i> <strong>Name:</strong> Empanada</p>' in response.data

    assert b'Empanada' in response.data