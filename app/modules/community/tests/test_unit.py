import pytest

from app import db
from app.modules.auth.models import User
from app.modules.profile.models import UserProfile
from app.modules.community.models import Community
from app.modules.community_join_request.models import CommunityJoinRequest
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


def test_sample_assertion(test_client):
    """
    Autor: Delfín Santana
    Test para comprobar que se estan poniendo los valores
    bien
    """
    test_user = db.session.get(
        User, 2
    )  # User.query.filter_by(email="user@example.com").first()
    assert test_user.email == "user@example.com"
    test_community = Community.query.filter_by(name="sample community").first()

    assert test_community.name == "sample community"
    assert test_community.url == "https://sample.com"
    assert test_community.description == "sample sample sample"
    assert test_user in test_community.members


def test_get_community_by_name(test_client):
    """
    Autor: Delfín Santana
    Debe de haber una función en el servicio para poder
    obtener una comunidad por su nombre
    """
    test_community = Community.query.filter_by(name="sample community").first()

    expected_community = service.get_community_by_name(test_community.name)
    assert test_community == expected_community


def test_get_community_by_id(test_client):
    """
    Autor: Delfín Santana
    Debe de haber una función en el servicio para poder
    obtener una comunidad por su id
    """
    test_community = Community.query.filter_by(name="sample community").first()

    expected_community = service.get_community_by_id(test_community.id)
    assert test_community == expected_community


def test_join_community_and_is_user_in_community(test_client):
    """
    Autor: Delfín Santana
    Debe de haber una función en el servicio para poder
    unirse a una comunidad y para poder comprobar que
    esta en la comunidad. En este test se prueban juntas
    para ver si funcionan bien cuando se ejecutan una
    detras de otra
    """
    test_user = User.query.filter_by(email="user_1@example.com").first()
    test_community = Community.query.filter_by(name="sample community").first()

    service.join_a_community(test_user, test_community)
    test_community = Community.query.filter_by(name="sample community").first()

    assert test_user in test_community.members


def test_is_user_in_community(test_client):
    """
    Autor: Delfín Santana
    Debe de haber una función en el servicio para poder
    comprobar si un usuario está en una comunidad
    """
    test_user = User.query.filter_by(email="user_1@example.com").first()
    test_community = Community.query.filter_by(name="sample community").first()

    result = service.is_user_in_community(test_user, test_community)

    assert result


def test_create_request(test_client):
    """
    Autor: Delfín Santana
    Debe de haber una función en el servicio para poder
    crear una request a una comunidad
    """
    test_user1 = db.session.get(User, 4)

    assert test_user1.email == "user_2@example.com"

    test_community = Community.query.filter_by(name="sample community").first()

    check_if_is_not_null = join_service.create_from_request(test_user1, test_community)
    assert check_if_is_not_null

    expected_request1 = CommunityJoinRequest.query.filter_by(
        user_who_wants_to_join_id=test_user1.id, community_id=test_community.id
    ).first()

    assert expected_request1

    assert expected_request1.user_who_wants_to_join_id == test_user1.id
    assert expected_request1.community_id == test_community.id


def test_create_request_when_already_in_community(test_client):
    """
    Autor: Delfín Santana
    Debe de haber una función en el servicio para poder
    crear una request a una comunidad, si el usuario
    ya esta en la comunidad, no debe de pasar nada
    """
    test_user3 = db.session.get(User, 3)

    assert test_user3.email == "user_1@example.com"

    test_community = Community.query.filter_by(name="sample community").first()

    check_if_is_null = join_service.create_from_request(test_user3, test_community)

    assert not check_if_is_null

    expected_request1 = CommunityJoinRequest.query.filter_by(
        user_who_wants_to_join_id=test_user3.id, community_id=test_community.id
    ).first()

    assert not expected_request1


def test_check_if_user_has_sent_a_request(test_client):
    """
    Autor: Delfín Santana
    Debe de haber una función en el servicio para poder
    comprobar si un usuario ha enviado una request a una
    comunidad, respondiendo correctamente dependiendo de
    si el usuario ya esta en la comunidad, o si ha enviado
    o no una solicitud
    """
    test_user1 = db.session.get(User, 3)
    test_user2 = db.session.get(User, 4)
    test_user3 = db.session.get(User, 5)

    assert test_user1
    assert test_user2
    assert test_user3

    test_community = Community.query.filter_by(name="sample community").first()
    result1 = join_service.has_user_sent_a_request(test_user1, test_community)
    result2 = join_service.has_user_sent_a_request(test_user2, test_community)
    result3 = join_service.has_user_sent_a_request(test_user3, test_community)

    assert not result1  # este usuario esta ya en la comunidad, por lo que es falso
    assert result2  # este usuario si que ha enviado una solicitud
    assert not result3  # este usuario no ha enviado solicitud


def test_get_all_request_sent_to_community(test_client):
    """
    Autor: Delfín Santana
    Debe de haber una función en el servicio para poder
    obtener todas las requests que se han enviado
    a una comunidad
    """
    test_user1 = db.session.get(User, 4)
    test_user2 = db.session.get(User, 5)

    test_community = Community.query.filter_by(name="sample community").first()

    check_if_is_not_null = join_service.create_from_request(test_user2, test_community)
    assert check_if_is_not_null

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert all_requests
    assert len(all_requests) == 2
    assert all_requests[0].user_who_wants_to_join_id == test_user1.id
    assert all_requests[1].user_who_wants_to_join_id == test_user2.id


def test_accept_request(test_client):
    """
    Autor: Delfín Santana
    Debe de haber una función en el servicio para poder
    aceptar una request
    """
    test_user1 = db.session.get(User, 4)
    test_user2 = db.session.get(User, 5)

    test_community = Community.query.filter_by(name="sample community").first()

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    expected_to_be_accepted_request = all_requests[0]
    join_service.accept_request(
        test_user1, test_community, expected_to_be_accepted_request
    )

    test_community = Community.query.filter_by(name="sample community").first()
    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert test_user1 in test_community.members
    assert len(all_requests) == 1
    assert all_requests[0].user_who_wants_to_join_id == test_user2.id


def test_accept_request_bad(test_client):
    """
    Autor: Delfín Santana
    Cuando se acepta una request de un usuario que no es quien
    la ha enviado, no debe de pasar nada
    """
    test_user1 = db.session.get(User, 4)
    test_user2 = db.session.get(User, 5)

    test_community = Community.query.filter_by(name="sample community").first()

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    expected_to_be_accepted_request = all_requests[0]
    expected_to_be_false = join_service.accept_request(
        test_user1, test_community, expected_to_be_accepted_request
    )

    test_community = Community.query.filter_by(name="sample community").first()
    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert test_user2 not in test_community.members
    assert not expected_to_be_false
    assert len(all_requests) == 1
    assert all_requests[0].user_who_wants_to_join_id == test_user2.id


def test_decline_request(test_client):
    """
    Autor: Delfín Santana
    Debe de haber una función en el servicio para poder
    declinar una request
    """
    test_user1 = db.session.get(User, 5)

    test_community = Community.query.filter_by(name="sample community").first()

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert len(all_requests) == 1

    expected_to_decline_request = all_requests[0]
    join_service.decline_request(expected_to_decline_request)

    test_community = Community.query.filter_by(name="sample community").first()
    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert test_user1 not in test_community.members
    assert len(all_requests) == 0


def test_route_communities_without_loggin_in(test_client):
    """
    Autor: Delfín Santana
    Cuando se accede a la ruta /community, se puede acceder y
    te debe de devolver todas las comunidades, aunque no estes
    logueado
    """
    response = test_client.get("/community")
    assert response.status_code == 200, "Communities page could not be accessed."
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


def test_route_communities(test_client):
    """
    Autor: Delfín Santana
    Cuando se accede a la ruta /community, se puede acceder y
    te debe de devolver todas las comunidades
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/community")
    assert response.status_code == 200, "Communities page could not be accessed."
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


def test_route_get_my_communities(test_client):
    """
    Autor: Delfín Santana
    Cuando se accede a la ruta /my_communities, se puede acceder y
    te debe de devolver las comunidades de las que eres miembro
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/my_communities")
    assert response.status_code == 200, "My communities page could not be accessed."
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


def test_route_get_my_communities_when_not_logged(test_client):
    """
    Autor: Delfín Santana
    Cuando se accede a la ruta /my_communities sin estar loguedado,
    te debe de redireccionar
    """
    response = test_client.get("/my_communities")
    assert (
        response.status_code == 302
    ), "No redirection occured when accesing to /my_communities without logging in."


def test_route_get_my_communities_when_not_in_any_community(test_client):
    """
    Autor: Delfín Santana
    Cuando se accede a la ruta /my_communities,
    no te debe de salir información de aquellas comunidades a las que no perteneces
    """
    login_response = login(test_client, "user_3@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/my_communities")
    assert response.status_code == 200, "My communities page could not be accessed."
    assert (
        b"sample community" not in response.data
    ), "The expected content is not present on the page"
    assert (
        b"https://sample.com" not in response.data
    ), "The expected content is not present on the page"
    assert (
        b"sample sample sample" not in response.data
    ), "The expected content is not present on the page"

    logout(test_client)


def test_route_get_specific_community(test_client):
    """
    Autor: Delfín Santana
    Cuando se accede a la ruta /community/<nombre de comunidad que existe>,
    te debe de salir información de la comunidad a la que se ha accedido
    especificamente. Pero no te debe de salir informacion de mas
    que esta reservado para otras vistas, como es la descripcion de la
    comunidad
    """
    response = test_client.get("/community/sample community/")
    assert (
        response.status_code == 200
    ), "Specific commumity view page could not be accessed."
    assert b"Join!" in response.data, "The expected content is not present on the page"
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


def test_route_get_specific_community_that_doesnt_exists(test_client):
    """
    Autor: Delfín Santana
    Cuando se accede a la ruta /community/<nombre de comunidad que NO existe>,
    te debe de salir un error 404
    """
    response = test_client.get("/community/blah_blah/")
    assert (
        response.status_code == 404
    ), "Specific commumity that doesn't exsits could be accessed."

    logout(test_client)


def test_route_get_specific_community_info(test_client):
    """
    Autor: Delfín Santana
    Cuando se accede a la ruta /community/<nombre de comunidad que existe>/info,
    te debe de salir información de la comunidad a la que se ha accedido
    especificamente. En especifico, su descripcion
    """
    response = test_client.get("/community/sample community/info")
    assert (
        response.status_code == 200
    ), "Specific commumity info view page could not be accessed."
    assert b"Join!" in response.data, "The expected content is not present on the page"
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


def test_route_get_specific_community_that_doesnt_exsits_info(test_client):
    """
    Autor: Delfín Santana
    Cuando se accede a la ruta /community/<nombre de comunidad que NO existe>/info,
    te debe de salir un error 404
    """
    response = test_client.get("/community/blah blah/info")
    assert (
        response.status_code == 404
    ), "Specific commumity that doesn't exists info view page could be accessed."

    logout(test_client)


def test_route_get_specific_community_members(test_client):
    """
    Autor: Delfín Santana
    Cuando se accede a la ruta /community/<nombre de comunidad que existe>/members,
    se debe de poder acceder
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/community/sample community/members")
    assert (
        response.status_code == 200
    ), "Specific commumity members view page could not be accessed."
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


def test_route_get_specific_community_members_when_not_logged_in(test_client):
    """
    Autor: Delfín Santana
    Cuando se accede a la ruta /community/<nombre de comunidad que existe>/members,
    cuando no estas registrado te debe de redireccionar
    """

    response = test_client.get("/community/sample community/members")
    assert (
        response.status_code == 302
    ), "Specific commumity memers view page could be accessed without loggin in."

    logout(test_client)


def test_route_get_specific_community_that_doesnt_exists_members(test_client):
    """
    Autor: Delfín Santana
    Cuando se accede a la ruta /community/<nombre de comunidad que NO existe>/members,
    debe de dar un error 404
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/community/blah blah/members")
    assert (
        response.status_code == 404
    ), "Specific commumity memers view page could be accessed without loggin in."

    logout(test_client)


def test_route_post_create_community(test_client):
    """
    Autor: Delfín Santana
    Se debe de poder crear una comunidad
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.post(
        "/community/create",
        data={
            "name": "new_community_just_created",
            "description_info": "This a new community",
            "url": "https://sample.sample.sample.com",
        },
    )
    assert response.status_code == 302, "Community could not be created."

    logout(test_client)

    community_test = service.get_community_by_name("new_community_just_created")

    assert community_test
    assert community_test.name == "new_community_just_created"
    assert community_test.description == "This a new community"
    assert community_test.url == "https://sample.sample.sample.com"
