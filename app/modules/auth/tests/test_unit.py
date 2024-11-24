import pytest
from flask import url_for
from unittest.mock import patch, MagicMock
from app import db
from werkzeug.security import check_password_hash
from app.modules.auth.services import AuthenticationService
from app.modules.auth.models import User, OAuthProvider
from app.modules.auth.repositories import UserRepository
from app.modules.profile.repositories import UserProfileRepository


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():

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

# TESTING OAuthProvider #


def test_service_create_oauth_provider_success(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "oauth_test@example.com",
        "password": "hashed_password",
        "oauth_provider": "google",
        "oauth_provider_user_id": "1234",
    }

    provider_data = {
        "oauth_provider": "github",
        "oauth_provider_user_id": "5678"
    }

    user = AuthenticationService().create_with_profile_and_oauth_provider_appended(**data)

    AuthenticationService().append_oauth_provider(user, **provider_data)

    user = UserRepository().get_by_email(data["email"])
    assert UserRepository().count() == 1
    assert UserProfileRepository().count() == 1
    assert len(user.oauth_providers) == 2


def test_service_create_oauth_provider_success_orcid(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "oauth_test@example.com",
        "password": "hashed_password",
        "oauth_provider": "google",
        "oauth_provider_user_id": "1234",
    }

    provider_data = {
        "oauth_provider": "orcid",
        "oauth_provider_user_id": "0000-0000-0000-0000",
    }

    user = AuthenticationService().create_with_profile_and_oauth_provider_appended(**data)

    AuthenticationService().append_oauth_provider(user, **provider_data)

    user = UserRepository().get_by_email(data["email"])
    assert UserRepository().count() == 1
    assert UserProfileRepository().count() == 1
    assert len(user.oauth_providers) == 2
    assert user.orcid == "0000-0000-0000-0000"


def test_service_create_with_profile_and_oauth_provider_success(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "oauth_test@example.com",
        "password": "hashed_password",
        "oauth_provider": "google",
        "oauth_provider_user_id": "1234",
    }

    AuthenticationService().create_with_profile_and_oauth_provider_appended(**data)

    assert UserRepository().count() == 1
    assert UserProfileRepository().count() == 1
    user = UserRepository().get_by_email(data["email"])
    assert user.oauth_providers[0].provider_name == "google"
    assert user.oauth_providers[0].provider_user_id == "1234"


def test_service_create_with_profile_and_oauth_provider_orcid_success(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "oauth_test@example.com",
        "password": "hashed_password",
        "oauth_provider": "orcid",
        "oauth_provider_user_id": "1234",
        "orcid": "0000-0000-0000-0000",
    }

    AuthenticationService().create_with_profile_and_oauth_provider_appended(**data)

    assert UserRepository().count() == 1
    assert UserProfileRepository().count() == 1
    user = UserRepository().get_by_orcid(data["orcid"])
    assert user.oauth_providers[0].provider_name == "orcid"
    assert user.oauth_providers[0].provider_user_id == "1234"
    assert user.orcid == "0000-0000-0000-0000"


def test_service_create_with_profile_and_oauth_provider_fail_no_email(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "",
        "password": "hashed_password",
        "oauth_provider": "google",
        "oauth_provider_user_id": "1234",
    }

    with pytest.raises(ValueError, match="Email is required."):
        AuthenticationService().create_with_profile_and_oauth_provider_appended(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


def test_service_create_with_profile_and_oauth_provider_fail_no_password(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "oauth_test@gmail.com",
        "oauth_provider": "google",
        "oauth_provider_user_id": "1234",
    }

    with pytest.raises(ValueError, match="Password is required."):
        AuthenticationService().create_with_profile_and_oauth_provider_appended(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


def test_service_create_with_profile_and_oauth_provider_fail_no_oauth_provider(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "oauth_example@gmail.com",
        "password": "hashed_password",
        "oauth_provider": "",
        "oauth_provider_user_id": "1234",
    }

    with pytest.raises(ValueError, match="OAuth provider is required."):
        AuthenticationService().create_with_profile_and_oauth_provider_appended(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0

# TESTING OAuth_provider GitHub #


def test_signup_github_no_signup_state(test_client):
    with test_client.session_transaction() as session:
        session["signup_state"] = None
    response = test_client.get(url_for("auth.sign_up_github"))
    assert response.status_code == 302
    assert response.location.endswith(url_for("auth.show_signup_form"))


@patch("app.modules.auth.routes.github.authorize_redirect")
def test_signup_github_redirect(mock_authorize_redirect, test_client):
    with test_client.session_transaction() as session:
        session["signup_state"] = "active"
    test_client.get(url_for("auth.sign_up_github"))
    mock_authorize_redirect.assert_called_once_with(url_for("auth.authorize_github", _external=True, flow="signup"))


@patch("app.modules.auth.routes.github.authorize_redirect")
def test_login_github_redirect(mock_authorize_redirect, test_client):
    with test_client.session_transaction() as session:
        session["login_state"] = "active"
    test_client.get(url_for("auth.login_github"))
    mock_authorize_redirect.assert_called_once_with(
        url_for("auth.authorize_github", _external=True, flow="login")
    )


@patch("app.modules.auth.routes.github.get")
@patch("app.modules.auth.routes.github.authorize_access_token")
@patch("app.modules.auth.routes.authentication_service")
def test_authorize_github_existing_user_with_provider(
    mock_auth_service, mock_authorize_access_token, mock_github_get, test_client, clean_database
):
    # Create a user with a GitHub provider
    user = User(email="test@example.com", password="hashed", oauth_providers=[])
    provider = OAuthProvider(provider_name="github", provider_user_id="12345", user=user)
    db.session.add(user)
    db.session.add(provider)
    db.session.commit()

    mock_authorize_access_token.return_value = None
    mock_github_get.return_value = MagicMock(
        json=lambda: {"email": "test@example.com", "id": "12345"}
    )
    mock_auth_service.get_by_email.return_value = user

    response = test_client.get(url_for("auth.authorize_github"))
    assert response.status_code == 302
    assert response.location.endswith(url_for("public.index"))


@patch("app.modules.auth.routes.github.authorize_access_token")
@patch("app.modules.auth.routes.github.get")
@patch("app.modules.auth.routes.authentication_service")
def test_authorize_github_new_user(
    mock_authorize_access_token, mock_github_get, mock_authentication_service, test_client, clean_database
):
    mock_authorize_access_token.return_value = None

    # Set up the mock to return the GitHub user data
    mock_github_get.return_value = MagicMock(
        json=lambda: {"email": "new@example.com", "id": "12345", "name": "John"}
    )

    # Set up the mock to return the user
    user = User(
        email="new@example.com",
        password="hashed",
        oauth_providers=[
            OAuthProvider(provider_name="github", provider_user_id="12345")
        ],)
    mock_authentication_service.get_by_email.return_value = None
    mock_authentication_service.create_with_profile_and_oauth_provider_appended.return_value = user

    response = test_client.get(url_for("auth.authorize_github"))
    assert response.status_code == 302
    assert response.location.endswith(url_for("public.index"))
