import os
from unittest.mock import MagicMock, patch
import pytest
from flask import url_for
from werkzeug.security import generate_password_hash
from app import db
from app.modules.auth.models import OAuthProvider, User
from app.modules.auth.services import AuthenticationService
from app.modules.auth.repositories import UserRepository
from app.modules.profile.repositories import UserProfileRepository


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        # Add HERE new elements to the database that you want to exist in the test context.
        # DO NOT FORGET to use db.session.add(<element>) and db.session.commit() to save the data.
        pass

    yield test_client


def test_login_success(test_client):
    response = test_client.post(
        "/login",
        data=dict(email="test@example.com", password="test1234"),
        follow_redirects=True,
    )

    assert response.request.path != url_for("auth.login"), "Login was unsuccessful"

    test_client.get("/logout", follow_redirects=True)


def test_login_unsuccessful_bad_email(test_client):
    response = test_client.post(
        "/login",
        data=dict(email="bademail@example.com", password="test1234"),
        follow_redirects=True,
    )

    assert response.request.path == url_for("auth.login"), "Login was unsuccessful"

    test_client.get("/logout", follow_redirects=True)


def test_login_unsuccessful_bad_password(test_client):
    response = test_client.post(
        "/login",
        data=dict(email="test@example.com", password="basspassword"),
        follow_redirects=True,
    )

    assert response.request.path == url_for("auth.login"), "Login was unsuccessful"

    test_client.get("/logout", follow_redirects=True)


def test_signup_user_no_name(test_client):
    response = test_client.post(
        "/signup",
        data=dict(surname="Foo", email="test@example.com", password="test1234"),
        follow_redirects=True,
    )
    assert response.request.path == url_for(
        "auth.show_signup_form"
    ), "Signup was unsuccessful"
    assert b"This field is required" in response.data, response.data


def test_signup_user_unsuccessful(test_client):
    email = "test@example.com"
    response = test_client.post(
        "/signup",
        data=dict(name="Test", surname="Foo", email=email, password="test1234"),
        follow_redirects=True,
    )
    assert response.request.path == url_for(
        "auth.show_signup_form"
    ), "Signup was unsuccessful"
    assert f"Email {email} in use".encode("utf-8") in response.data


def test_signup_user_successful(test_client):
    response = test_client.post(
        "/signup",
        data=dict(
            name="Foo", surname="Example", email="foo@example.com", password="foo1234"
        ),
        follow_redirects=True,
    )
    assert response.request.path == url_for("public.index"), "Signup was unsuccessful"


def test_service_create_with_profie_success(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "service_test@example.com",
        "password": "test1234",
    }

    AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 1
    assert UserProfileRepository().count() == 1


def test_service_create_with_profile_fail_no_email(clean_database):
    data = {"name": "Test", "surname": "Foo", "email": "", "password": "1234"}

    with pytest.raises(ValueError, match="Email is required."):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


def test_service_create_with_profile_fail_no_password(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "test@example.com",
        "password": "",
    }

    with pytest.raises(ValueError, match="Password is required."):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


@patch("app.modules.auth.routes.github")
@patch("app.modules.auth.routes.authentication_service")
def test_authorize_github_signup(mock_auth_service, mock_github, test_client):
    mock_github.authorize_access_token.return_value = {"access_token": "fake_token"}
    mock_github.token = {"access_token": "fake_token"}
    mock_github.get.side_effect = [
        MagicMock(json=lambda: {"email": "test@example.com", "id": "github_id"}),
        MagicMock(
            json=lambda: [
                {"email": "test@example.com", "primary": True, "verified": True}
            ]
        ),
    ]
    mock_auth_service.get_by_email.return_value = None
    mock_auth_service.create_with_profile_and_oauth_provider_appended.return_value = (
        MagicMock(get_id=lambda: "mock_user_id")
    )

    with test_client.session_transaction() as sess:
        sess["signup_state"] = "test_state"
        sess["origin_url"] = "/dataset/upload"

    response = test_client.get("/authorize/github?flow=signup")

    assert response.status_code == 302
    assert response.location == "/dataset/upload#githubToken=fake_token"


@patch("app.modules.auth.routes.github")
@patch("app.modules.auth.routes.authentication_service")
def test_authorize_github_login(mock_auth_service, mock_github, test_client):
    mock_github.authorize_access_token.return_value = None
    mock_github.token = {"access_token": "fake_token"}
    mock_github.get.side_effect = [
        MagicMock(json=lambda: {"email": "test@example.com", "id": "github_id"}),
        MagicMock(
            json=lambda: [
                {"email": "test@example.com", "primary": True, "verified": True}
            ]
        ),
    ]
    mock_user = MagicMock()
    mock_user.oauth_providers = []
    mock_auth_service.get_by_email.return_value = mock_user
    mock_user.get_id.return_value = "mock_user_id"

    with test_client.session_transaction() as sess:
        sess["login_state"] = "test_state"
        sess["origin_url"] = "/dataset/upload"

    response = test_client.get("/authorize/github?flow=login")

    assert response.status_code == 302
    assert response.location == "/dataset/upload#githubToken=fake_token"


def test_get_github_repositories_no_token(test_client):
    with test_client.session_transaction() as sess:
        sess["github_token"] = None
    response = test_client.get("/github/repositories")
    assert response.status_code == 401
    assert response.json == {"error": "No authentication token found"}


@patch("app.modules.auth.routes.requests.get")
@patch.dict("os.environ", {"GITHUB_TEST_TOKEN": "test_token"})
def test_get_github_repositories_success(mock_get, test_client):
    mock_response = {
        "status_code": 200,
        "json.return_value": [
            {"id": 1, "name": "repo1", "full_name": "user/repo1"},
            {"id": 2, "name": "repo2", "full_name": "user/repo2"},
        ],
    }

    class MockResponse:
        def __init__(self, status_code, json_data):
            self.status_code = status_code
            self._json_data = json_data

        def json(self):
            return self._json_data

    mock_get.return_value = MockResponse(
        status_code=mock_response["status_code"],
        json_data=mock_response["json.return_value"],
    )

    mock_get.return_value = MockResponse(
        status_code=mock_response["status_code"],
        json_data=mock_response["json.return_value"],
    )

    with test_client.session_transaction() as sess:
        sess["github_token"] = os.getenv("GITHUB_TEST_TOKEN")

    response = test_client.get("/github/repositories")
    assert response.status_code == 200
    assert response.json == [
        {"id": 1, "name": "repo1", "full_name": "user/repo1"},
        {"id": 2, "name": "repo2", "full_name": "user/repo2"},
    ]


@patch("app.modules.auth.routes.requests.get")
@patch.dict("os.environ", {"GITHUB_TEST_TOKEN": "test_token"})
def test_get_github_repositories_failure(mock_get, test_client):
    mock_response = {
        "status_code": 500,
        "json.return_value": {"error": "Failed to fetch repositories"},
    }
    mock_get.return_value = type("MockResponse", (object,), mock_response)

    with test_client.session_transaction() as sess:
        sess["github_token"] = os.getenv("GITHUB_TEST_TOKEN")

    response = test_client.get("/github/repositories")
    assert response.status_code == 500
    assert response.json == {"error": "Failed to fetch repositories"}


@patch("app.modules.auth.routes.gitlab")
@patch("app.modules.auth.routes.authentication_service")
def test_authorize_gitlab_signup(mock_auth_service, mock_gitlab, test_client):
    mock_gitlab.authorize_access_token.return_value = None
    mock_gitlab.token = {"access_token": "fake_token"}
    mock_gitlab.get.side_effect = [
        MagicMock(json=lambda: {"email": "test@example.com", "id": "gitlab_id"}),
        MagicMock(
            json=lambda: [
                {"email": "test@example.com", "primary": True, "verified": True}
            ]
        ),
    ]
    mock_auth_service.get_by_email.return_value = None
    mock_auth_service.create_with_profile_and_oauth_provider_appended.return_value = (
        MagicMock(get_id=lambda: "mock_user_id")
    )

    with test_client.session_transaction() as sess:
        sess["signup_state"] = "test_state"
        sess["origin_url"] = "/dataset/upload"

    response = test_client.get("/authorize/gitlab?flow=signup")

    assert response.status_code == 302
    assert response.location == "/dataset/upload#gitlabToken=fake_token"


@patch("app.modules.auth.routes.gitlab")
@patch("app.modules.auth.routes.authentication_service")
def test_authorize_gitlab_login(mock_auth_service, mock_gitlab, test_client):
    mock_gitlab.authorize_access_token.return_value = None
    mock_gitlab.token = {"access_token": "fake_token"}
    mock_gitlab.get.side_effect = [
        MagicMock(json=lambda: {"email": "test@example.com", "id": "gitlab_id"}),
        MagicMock(
            json=lambda: [
                {"email": "test@example.com", "primary": True, "verified": True}
            ]
        ),
    ]
    mock_user = MagicMock()
    mock_user.oauth_providers = []
    mock_auth_service.get_by_email.return_value = mock_user
    mock_user.get_id.return_value = "mock_user_id"

    with test_client.session_transaction() as sess:
        sess["login_state"] = "test_state"
        sess["origin_url"] = "/dataset/upload"

    response = test_client.get("/authorize/gitlab?flow=login")

    assert response.status_code == 302
    assert response.location == "/dataset/upload#gitlabToken=fake_token"


def test_get_gitlab_repositories_no_token(test_client):
    with test_client.session_transaction() as sess:
        sess["gitlab_token"] = None
    response = test_client.get("/gitlab/repositories")
    assert response.status_code == 401
    assert response.json == {"error": "No authentication token found"}


@patch("app.modules.auth.routes.requests.get")
@patch.dict("os.environ", {"GITLAB_TEST_TOKEN": "test_token"})
def test_get_gitlab_repositories_success(mock_get, test_client):
    mock_response = {
        "status_code": 200,
        "json.return_value": [
            {"id": 1, "name": "repo1", "path_with_namespace": "user/repo1"},
            {"id": 2, "name": "repo2", "path_with_namespace": "user/repo2"},
        ],
    }

    class MockResponse:
        def __init__(self, status_code, json_data):
            self.status_code = status_code
            self._json_data = json_data

        def json(self):
            return self._json_data

    mock_get.return_value = MockResponse(
        status_code=mock_response["status_code"],
        json_data=mock_response["json.return_value"],
    )

    mock_get.return_value = MockResponse(
        status_code=mock_response["status_code"],
        json_data=mock_response["json.return_value"],
    )

    with test_client.session_transaction() as sess:
        sess["gitlab_token"] = os.getenv("GITLAB_TEST_TOKEN")

    response = test_client.get("/gitlab/repositories")
    assert response.status_code == 200
    assert response.json == [
        {"id": 1, "name": "repo1", "full_name": "user/repo1"},
        {"id": 2, "name": "repo2", "full_name": "user/repo2"},
    ]


@patch("app.modules.auth.routes.requests.get")
@patch.dict("os.environ", {"GITLAB_TEST_TOKEN": "test_token"})
def test_get_gitlab_repositories_failure(mock_get, test_client):
    mock_response = {
        "status_code": 500,
        "json.return_value": {"error": "Failed to fetch repositories"},
    }
    mock_get.return_value = type("MockResponse", (object,), mock_response)

    with test_client.session_transaction() as sess:
        sess["gitlab_token"] = os.getenv("GITLAB_TEST_TOKEN")

    response = test_client.get("/gitlab/repositories")
    assert response.status_code == 500
    assert response.json == {"error": "Failed to fetch repositories"}


@patch("app.modules.auth.routes.orcid")
@patch("app.modules.auth.routes.authentication_service")
@patch("app.modules.auth.routes.current_user")
def test_authorize_signup_orcid_with_email(
    mock_current_user, mock_auth_service, mock_orcid, test_client
):
    # Simula que el usuario no está autenticado
    mock_current_user.is_authenticated = False

    # Simula la autorización del token con ORCID
    mock_orcid.authorize_access_token.return_value = {
        "access_token": "fake_token",
        "orcid": "0000-0002-1825-0097",
    }

    # Simula las respuestas de los endpoints de ORCID
    mock_orcid.get.side_effect = [
        MagicMock(
            json=lambda: {
                "person": {
                    "name": {
                        "given-names": {"value": "John"},
                        "family-name": {"value": "Doe"},
                    }
                }
            }
        ),
        MagicMock(
            json=lambda: {
                "email": [
                    {"email": "test@example.com", "primary": True, "verified": True}
                ]
            }
        ),
    ]

    # Mock del servicio para verificar el email
    mock_user = None  # Simula que el usuario no existe
    mock_auth_service.get_by_email.return_value = mock_user

    # Crea un mock de usuario que no cause problemas de serialización
    mock_created_user = MagicMock()
    mock_created_user.get_id.return_value = "mock_user_id"
    mock_created_user.is_active = True
    mock_created_user.email = "test@example.com"
    mock_auth_service.create_with_profile_and_oauth_provider_appended.return_value = (
        mock_created_user
    )

    # Simula el estado de la sesión
    with test_client.session_transaction() as sess:
        sess["signup_state"] = "test_state"

    # Ejecuta la solicitud
    response = test_client.get("/authorize/signup/orcid?state=test_state")

    # Verificaciones
    assert response.status_code == 302
    assert response.location == "/"  # Redirige a la página principal

    # Verifica que los servicios fueron llamados correctamente
    assert mock_auth_service.get_by_email.called
    assert mock_auth_service.create_with_profile_and_oauth_provider_appended.called


@patch("app.modules.auth.routes.orcid")
@patch("app.modules.auth.routes.authentication_service")
@patch("app.modules.auth.routes.current_user")
def test_authorize_signup_orcid_no_email(
    mock_current_user, mock_auth_service, mock_orcid, test_client
):
    # Simula que el usuario no está autenticado
    mock_current_user.is_authenticated = False

    # Simula la autorización del token con ORCID
    mock_orcid.authorize_access_token.return_value = {
        "access_token": "fake_token",
        "orcid": "0000-0002-1825-0097",
    }

    # Simula las respuestas de ORCID
    mock_orcid.get.side_effect = [
        MagicMock(
            json=lambda: {
                "person": {
                    "name": {
                        "given-names": {"value": "John"},
                        "family-name": {"value": "Doe"},
                    }
                }
            }
        ),
        MagicMock(json=lambda: {"email": []}),  # Email vacío
    ]

    # Simula el estado de la sesión
    with test_client.session_transaction() as sess:
        sess["signup_state"] = "test_state"

    # Ejecuta la solicitud
    response = test_client.get("/authorize/signup/orcid?state=test_state")

    # Verificaciones
    assert response.status_code == 302
    assert response.location == "/provide_email"


@patch("app.modules.auth.routes.orcid")
@patch("app.modules.auth.routes.authentication_service")
@patch("app.modules.auth.routes.current_user")
def test_authorize_login_orcid_success(
    mock_current_user, mock_auth_service, mock_orcid, test_client
):
    # Simula que el usuario no está autenticado
    mock_current_user.is_authenticated = False

    # Simula la autorización del token con ORCID
    mock_orcid.authorize_access_token.return_value = {
        "access_token": "fake_token",
        "orcid": "0000-0002-1825-0097",
    }

    # Mock del usuario existente en la base de datos
    mock_user = MagicMock()
    mock_user.get_id.return_value = "mock_user_id"
    mock_user.is_active = True  # Necesario para Flask-Login
    mock_user.email = "test@example.com"
    mock_auth_service.get_by_orcid.return_value = mock_user

    # Simula el estado de la sesión
    with test_client.session_transaction() as sess:
        sess["login_state"] = "test_state"

    # Ejecuta la solicitud al endpoint
    response = test_client.get("/authorize/login/orcid?state=test_state")

    # Verificaciones
    assert response.status_code == 302
    assert response.location == "/"  # Redirige a la página principal
    mock_auth_service.get_by_orcid.assert_called_once_with("0000-0002-1825-0097")


@patch("app.modules.auth.routes.authentication_service")
def test_provide_email_success(mock_auth_service, test_client):
    mock_user = MagicMock()
    mock_user.is_active = True
    mock_user.get_id.return_value = "mock_user_id"

    mock_auth_service.get_by_email.return_value = None
    mock_auth_service.create_with_profile_and_oauth_provider_appended.return_value = (
        mock_user
    )

    with test_client.session_transaction() as sess:
        sess["orcid_id"] = "0000-0002-1825-0097"
        sess["profile_data"] = {"given_name": "John", "family_name": "Doe"}

    response = test_client.post(
        "/provide_email",
        data={"email": "test@example.com"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert mock_auth_service.create_with_profile_and_oauth_provider_appended.called


def test_create_with_profile_and_oauth_provider_success(clean_database):
    data = {
        "email": "test@example.com",
        "password": "fake_password",
        "name": "John",
        "surname": "Doe",
        "oauth_provider": "orcid",
        "oauth_provider_user_id": "0000-0002-1825-0097",
        "orcid": "0000-0002-1825-0097",
    }

    auth_service = AuthenticationService()
    user = auth_service.create_with_profile_and_oauth_provider_appended(**data)

    assert user.email == data["email"]
    assert user.orcid == data["orcid"]
    assert user.oauth_providers[0].provider_name == "orcid"


def test_set_password_and_check_password():
    user = User(email="test@example.com")
    user.set_password("secure_password")
    assert user.check_password("secure_password") is True
    assert user.check_password("wrong_password") is False


def test_is_oauth_user_false():
    user = User(email="test@example.com", password=generate_password_hash("password"))
    assert user.is_oauth_user() is False


def test_is_oauth_user_true():
    user = User(email="test@example.com", password=generate_password_hash("password"))
    oauth_provider = OAuthProvider(provider_name="google", provider_user_id="12345")
    user.oauth_providers.append(oauth_provider)
    db.session.add(user)
    db.session.add(oauth_provider)
    db.session.commit()
    assert user.is_oauth_user() is True


@patch("app.modules.auth.routes.google")
@patch("app.modules.auth.routes.authentication_service")
@patch("app.modules.auth.routes.current_user")
def test_login_google_success(
    mock_current_user, mock_auth_service, mock_google, test_client
):
    mock_current_user.is_authenticated = False

    with test_client.session_transaction() as sess:
        sess["login_state"] = "test_state"

    mock_google.authorize_access_token.return_value = {"access_token": "fake_token"}
    mock_google.get.return_value.json.return_value = {
        "email": "test@example.com",
        "sub": "google_id",
    }

    mock_user = MagicMock()
    mock_user.is_active = True
    mock_user.get_id.return_value = "mock_user_id"
    mock_auth_service.get_by_email.return_value = mock_user

    response = test_client.get("/authorize/login/google?state=test_state")

    assert response.status_code == 302
    assert response.location == "/"
    mock_auth_service.get_by_email.assert_called_once_with("test@example.com")


@patch("app.modules.auth.routes.google")
@patch("app.modules.auth.routes.authentication_service")
@patch("app.modules.auth.routes.current_user")
def test_signup_google_new_user(
    mock_current_user, mock_auth_service, mock_google, test_client
):
    # Simula que el usuario no está autenticado
    mock_current_user.is_authenticated = False

    # Configura el estado de la sesión para signup
    with test_client.session_transaction() as sess:
        sess["signup_state"] = "test_state"

    # Mock del flujo de OAuth con Google
    mock_google.authorize_access_token.return_value = {"access_token": "fake_token"}
    mock_google.get.return_value.json.return_value = {
        "email": "newuser@example.com",
        "sub": "google_id",
        "given_name": "John",
        "family_name": "Doe",
    }

    # Simula que el usuario no existe
    mock_auth_service.get_by_email.return_value = None

    # Configura el objeto devuelto por el método de creación
    mock_user = MagicMock()
    mock_user.get_id.return_value = "mock_user_id"
    mock_user.is_active = True
    mock_user.email = "newuser@example.com"
    mock_auth_service.create_with_profile_and_oauth_provider_appended.return_value = (
        mock_user
    )

    # Prueba el endpoint
    response = test_client.get("/authorize/signup/google?state=test_state")

    # Verificaciones
    assert response.status_code == 302
    assert response.location == "/"  # Redirige a la página principal
    mock_auth_service.get_by_email.assert_called_once_with("newuser@example.com")
    assert mock_auth_service.create_with_profile_and_oauth_provider_appended.called
