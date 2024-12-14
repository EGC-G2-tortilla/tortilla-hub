import pytest

from app import db
from app.modules.auth.models import User
from app.modules.profile.models import UserProfile
from app.modules.community.models import Community
from app.modules.community.services import CommunityService
from app.modules.community_join_request.services import CommunityJoinRequestService
from app.modules.conftest import login, logout

service = CommunityService()
join_service = CommunityJoinRequestService()


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        user_test = User(email="user@example.com", password="test1234")
        db.session.add(user_test)

        user_profile_test = UserProfile(
            user=user_test,
            orcid="1234",
            affiliation="sample",
            name="sample0",
            surname="sample_sample0",
        )
        db.session.add(user_profile_test)

        user_test1 = User(email="user_1@example.com", password="test1234")
        db.session.add(user_test1)

        user_profile_test1 = UserProfile(
            user=user_test1,
            orcid="1234",
            affiliation="sample",
            name="sample1",
            surname="sample_sample1",
        )
        db.session.add(user_profile_test1)

        user_test2 = User(email="user_2@example.com", password="test1234")
        db.session.add(user_test2)

        user_profile_test2 = UserProfile(
            user=user_test2,
            orcid="1234",
            affiliation="sample",
            name="sample2",
            surname="sample_sample2",
        )
        db.session.add(user_profile_test2)

        user_test3 = User(email="user_3@example.com", password="test1234")
        db.session.add(user_test3)

        user_profile_test3 = UserProfile(
            user=user_test3,
            orcid="1234",
            affiliation="sample",
            name="sample3",
            surname="sample_sample3",
        )
        db.session.add(user_profile_test3)
        db.session.commit()

        community_test = Community(
            name="sample community",
            admin=user_test.id,
            url="https://sample.com",
            description="sample sample sample",
        )
        community_test.members.append(user_test)
        db.session.add(community_test)
        db.session.commit()

    yield test_client


def test_route_join_community(test_client):
    """
    Autor: Delfín Santana
    Se debe de poder mandar una request para unirse a una comunidad
    """
    test_user = db.session.get(User, 5)
    assert test_user.email == "user_3@example.com"

    test_community = Community.query.filter_by(name="sample community").first()

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 0

    login_response = login(test_client, "user_3@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.post("/community/sample community/join")
    assert (
        response.status_code == 302
    ), "Specific commumity view page could not be accessed."

    logout(test_client)

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 1
    assert all_requests[0].user_who_wants_to_join_id == test_user.id


def test_route_get_specific_community_after_sending_request_to_join(test_client):
    """
    Autor: Delfín Santana
    Cuando se acceda a la vista de la comunidad a la que he mandado
    solicitud de unirme, la vista debe de mostrar que he mandado la solicitud
    """
    login_response = login(test_client, "user_3@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/community/sample community/")
    assert (
        response.status_code == 200
    ), "Specific commumity view page could not be accessed."
    assert (
        b"Join!" not in response.data
    ), "The expected content is not present on the page"
    assert (
        b"Waiting to be accepted by the administrator" in response.data
    ), "The expected content is not present on the page"
    assert (
        b"sample community" in response.data
    ), "The expected content is not present on the page"
    assert (
        b"https://sample.com" in response.data
    ), "The expected content is not present on the page"
    assert (
        b"sample sample sample" not in response.data
    ), "The expected content is not present on the page"

    logout(test_client)


def test_route_get_specific_community_info_after_sending_request_to_join(test_client):
    """
    Autor: Delfín Santana
    Cuando se acceda a la vista de info de la comunidad a la que he mandado
    solicitud de unirme, la vista debe de mostrar que he mandado la solicitud
    """
    login_response = login(test_client, "user_3@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/community/sample community/info")
    assert (
        response.status_code == 200
    ), "Specific commumity view page could not be accessed."
    assert (
        b"Join!" not in response.data
    ), "The expected content is not present on the page"
    assert (
        b"Waiting to be accepted by the administrator" in response.data
    ), "The expected content is not present on the page"
    assert (
        b"sample community" in response.data
    ), "The expected content is not present on the page"
    assert (
        b"https://sample.com" in response.data
    ), "The expected content is not present on the page"
    assert (
        b"sample sample sample" in response.data
    ), "The expected content is not present on the page"

    logout(test_client)


def test_route_get_specific_community_members_after_sending_request_to_join(
    test_client,
):
    """
    Autor: Delfín Santana
    Cuando se acceda a la vista de members de la comunidad a la que he mandado
    solicitud de unirme, la vista debe de mostrar que he mandado la solicitud
    """
    login_response = login(test_client, "user_3@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/community/sample community/members")
    assert (
        response.status_code == 200
    ), "Specific commumity view page could not be accessed."
    assert (
        b"Join!" not in response.data
    ), "The expected content is not present on the page"
    assert (
        b"Waiting to be accepted by the administrator" in response.data
    ), "The expected content is not present on the page"
    assert (
        b"sample community" in response.data
    ), "The expected content is not present on the page"
    assert (
        b"https://sample.com" in response.data
    ), "The expected content is not present on the page"
    assert (
        b"sample sample sample" not in response.data
    ), "The expected content is not present on the page"

    logout(test_client)


def test_route_get_specific_community_members_being_admin_after_sending_request_to_join(
    test_client,
):
    """
    Autor: Delfín Santana
    Cuando se acceda a la vista de members de la comunidad a la que he mandado
    solicitud de unirme, la vista debe de mostrar que he mandado la solicitud
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/community/sample community/members")
    assert (
        response.status_code == 200
    ), "Specific commumity view page could not be accessed."
    assert b"Accept" in response.data, "The expected content is not present on the page"
    assert (
        b"Decline" in response.data
    ), "The expected content is not present on the page"
    assert (
        b"sample community" in response.data
    ), "The expected content is not present on the page"
    assert (
        b"https://sample.com" in response.data
    ), "The expected content is not present on the page"
    assert (
        b"sample sample sample" not in response.data
    ), "The expected content is not present on the page"

    logout(test_client)


def test_route_decline_join_request_when_I_am_not_admin(test_client):
    """
    Autor: Delfín Santana
    Cuando se intenta denegar una solicitud de unirse a una comunidad sin ser el admin
    de esa comunidad se devuelve un codigo 503
    """
    test_user = db.session.get(User, 5)
    assert test_user.email == "user_3@example.com"

    test_community = Community.query.filter_by(name="sample community").first()

    assert test_community.admin != test_user.id

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 1
    assert all_requests[0].user_who_wants_to_join_id == test_user.id

    request_id = all_requests[0].id

    login_response = login(test_client, "user_3@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.post(
        "/community-join-request/" + str(request_id) + "/accept"
    )
    assert (
        response.status_code == 503
    ), "Join request could be declined by someone that is not admin."

    logout(test_client)

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 1
    assert all_requests[0].user_who_wants_to_join_id == test_user.id
    assert all_requests[0].id == request_id

    test_community = Community.query.filter_by(name="sample community").first()

    assert test_community.name == "sample community"
    assert test_user not in test_community.members


def test_route_decline_join_request_that_doenst_exists(test_client):
    """
    Autor: Delfín Santana
    Cuando se intenta denegar una solicitud de unirse a una comunidad, y la
    solicitud no existe, se devuelve el codigo 404
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.post("/community-join-request/100/decline")
    assert (
        response.status_code == 404
    ), "Join request that doesnt exsits could be declined."

    logout(test_client)


def test_route_decline_join_request(test_client):
    """
    Autor: Delfín Santana
    Se debe de poder declinar una request de unirse a una comunidad
    siendo admin a traves de una ruta
    """
    test_user = db.session.get(User, 5)
    assert test_user.email == "user_3@example.com"

    test_community = Community.query.filter_by(name="sample community").first()

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 1
    assert all_requests[0].user_who_wants_to_join_id == test_user.id

    request_id = all_requests[0].id

    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.post(
        "/community-join-request/" + str(request_id) + "/decline"
    )
    assert (
        response.status_code == 302
    ), "Specific commumity view page could not be accessed."

    logout(test_client)

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 0


def test_route_join_community_after_being_declined(test_client):
    """
    Autor: Delfín Santana
    Se debe de poder enviar una ruta para unirse a una comunidad despues de ser rechazado
    """
    test_user = db.session.get(User, 5)
    assert test_user.email == "user_3@example.com"

    test_community = Community.query.filter_by(name="sample community").first()

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 0

    login_response = login(test_client, "user_3@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.post("/community/sample community/join")
    assert (
        response.status_code == 302
    ), "Specific commumity view page could not be accessed."

    logout(test_client)

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 1
    assert all_requests[0].user_who_wants_to_join_id == test_user.id


def test_route_accept_join_request_when_I_am_not_admin(test_client):
    """
    Autor: Delfín Santana
    Cuando se intenta aceptar una solicitud de unirse a una comunidad sin ser el admin
    de esa comunidad se devuelve un codigo 503
    """
    test_user = db.session.get(User, 5)
    assert test_user.email == "user_3@example.com"

    test_community = Community.query.filter_by(name="sample community").first()

    assert test_community.admin != test_user.id

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 1
    assert all_requests[0].user_who_wants_to_join_id == test_user.id

    request_id = all_requests[0].id

    login_response = login(test_client, "user_3@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.post(
        "/community-join-request/" + str(request_id) + "/accept"
    )
    assert (
        response.status_code == 503
    ), "Join request could be accepted by someone that is not admin."

    logout(test_client)

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 1
    assert all_requests[0].user_who_wants_to_join_id == test_user.id
    assert all_requests[0].id == request_id

    test_community = Community.query.filter_by(name="sample community").first()

    assert test_community.name == "sample community"
    assert test_user not in test_community.members


def test_route_accept_join_request_that_doenst_exists(test_client):
    """
    Autor: Delfín Santana
    Cuando se intenta aceptar una solicitud de unirse a una comunidad, y la
    solicitud no existe, se devuelve el codigo 404
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.post("/community-join-request/100/accept")
    assert (
        response.status_code == 404
    ), "Join request that doesn't exists could be accepted."

    logout(test_client)


def test_route_accept_join_request(test_client):
    """
    Autor: Delfín Santana
    Se debe de poder aceptara una request de unirse a una comunidad
    siendo admin a traves de una ruta
    """
    test_user = db.session.get(User, 5)
    assert test_user.email == "user_3@example.com"

    test_community = Community.query.filter_by(name="sample community").first()

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 1
    assert all_requests[0].user_who_wants_to_join_id == test_user.id

    request_id = all_requests[0].id

    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.post(
        "/community-join-request/" + str(request_id) + "/accept"
    )
    assert (
        response.status_code == 302
    ), "Specific commumity view page could not be accessed."

    logout(test_client)

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 0

    test_community = Community.query.filter_by(name="sample community").first()

    assert test_community.name == "sample community"
    assert test_user in test_community.members


def test_route_join_community_when_already_in_community(test_client):
    """
    Autor: Delfín Santana
    Cuando se intenta crear una solicitud de unirse a una comunidad a la que ya se pertenece
    no pasa nada
    """
    test_user = db.session.get(User, 5)
    assert test_user.email == "user_3@example.com"

    test_community = Community.query.filter_by(name="sample community").first()

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 0

    login_response = login(test_client, "user_3@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.post("/community/sample community/join")
    assert (
        response.status_code == 302
    ), "Specific commumity view page could not be accessed."

    logout(test_client)

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 0


def test_route_join_community_that_doesnt_exists(test_client):
    """
    Autor: Delfín Santana
    Cuando se intenta crear una solicitud de unirse a una comunidad que no existe
    se devuelve un codigo 404
    """
    login_response = login(test_client, "user_3@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.post("/community/community_that_doesnt_exists/join")
    assert (
        response.status_code == 404
    ), "Specific commumity that doesn't exists could be accessed."
