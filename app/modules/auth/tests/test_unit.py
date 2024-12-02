from unittest.mock import MagicMock, patch
import pytest
from flask import url_for

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


@patch('app.modules.auth.routes.github')
@patch('app.modules.auth.routes.authentication_service')
def test_authorize_github_signup(mock_auth_service, mock_github, test_client):
    mock_github.authorize_access_token.return_value = {"access_token": "fake_token"}
    mock_github.token = {"access_token": "fake_token"}
    mock_github.get.side_effect = [
        MagicMock(json=lambda: {"email": "test@example.com", "id": "github_id"}),
        MagicMock(json=lambda: [{"email": "test@example.com", "primary": True, "verified": True}])
    ]
    mock_auth_service.get_by_email.return_value = None
    mock_auth_service.create_with_profile_and_oauth_provider_appended.return_value = MagicMock()

    with test_client.session_transaction() as sess:
        sess['signup_state'] = 'test_state'
        sess['origin_url'] = '/dataset/upload'

    response = test_client.get('/authorize/github?flow=signup')

    assert response.status_code == 302
    assert response.location == '/dataset/upload#githubToken=fake_token'


@patch('app.modules.auth.routes.github')
@patch('app.modules.auth.routes.authentication_service')
def test_authorize_github_login(mock_auth_service, mock_github, test_client):
    mock_github.authorize_access_token.return_value = None
    mock_github.token = {"access_token": "fake_token"}
    mock_github.get.side_effect = [
        MagicMock(json=lambda: {"email": "test@example.com", "id": "github_id"}),
        MagicMock(json=lambda: [{"email": "test@example.com", "primary": True, "verified": True}])
    ]
    mock_user = MagicMock()
    mock_user.oauth_providers = []
    mock_auth_service.get_by_email.return_value = mock_user
    mock_user.get_id.return_value = "mock_user_id"

    with test_client.session_transaction() as sess:
        sess['login_state'] = 'test_state'
        sess['origin_url'] = '/dataset/upload'

    response = test_client.get('/authorize/github?flow=login')

    assert response.status_code == 302
    assert response.location == '/dataset/upload#githubToken=fake_token'
