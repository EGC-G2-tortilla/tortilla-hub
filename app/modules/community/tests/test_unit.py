import pytest

from app import db
from app.modules.auth.models import User
from app.modules.community.models import Community
from app.modules.community_join_request.models import CommunityJoinRequest
from app.modules.community.services import CommunityService
from app.modules.community_join_request.services import CommunityJoinRequestService

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

        user_test1 = User(email="user_1@example.com", password="test1234")
        db.session.add(user_test1)

        user_test2 = User(email="user_2example.com", password="test1234")
        db.session.add(user_test2)

        user_test3 = User(email="user_3example.com", password="test1234")
        db.session.add(user_test3)
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
    Sample test to verify that the test framework and environment are working correctly.
    It does not communicate with the Flask application; it only performs a simple assertion to
    confirm that the tests in this module can be executed.
    """
    test_user = db.session.get(User, 2)  # User.query.filter_by(email="user@example.com").first()
    assert test_user.email == "user@example.com"
    test_community = Community.query.filter_by(name="sample community").first()

    assert test_community.name == "sample community"
    assert test_community.url == "https://sample.com"
    assert test_community.description == "sample sample sample"
    assert test_user in test_community.members


def test_get_community_by_name(test_client):
    test_community = Community.query.filter_by(name="sample community").first()

    expected_community = service.get_community_by_name(test_community.name)
    assert test_community == expected_community


def test_get_community_by_id(test_client):
    test_community = Community.query.filter_by(name="sample community").first()

    expected_community = service.get_community_by_id(test_community.id)
    assert test_community == expected_community


def test_join_community_and_is_user_in_community(test_client):
    test_user = User.query.filter_by(email="user_1@example.com").first()
    test_community = Community.query.filter_by(name="sample community").first()

    service.join_a_community(test_user, test_community)
    test_community = Community.query.filter_by(name="sample community").first()

    assert test_user in test_community.members


def test_is_user_in_community(test_client):
    test_user = User.query.filter_by(email="user_1@example.com").first()
    test_community = Community.query.filter_by(name="sample community").first()

    result = service.is_user_in_community(test_user, test_community)

    assert result


def test_create_request(test_client):
    test_user1 = db.session.get(User, 4)
    test_user3 = db.session.get(User, 3)

    assert test_user1
    assert test_user3

    test_community = Community.query.filter_by(name="sample community").first()

    check_if_is_not_null = join_service.create_from_request(test_user1, test_community)
    assert check_if_is_not_null

    check_if_is_null = join_service.create_from_request(test_user3, test_community)

    assert not check_if_is_null

    expected_request1 = CommunityJoinRequest.query.filter_by(user_who_wants_to_join_id=test_user1.id,
                                                             community_id=test_community.id).first()

    assert expected_request1

    assert expected_request1.user_who_wants_to_join_id == test_user1.id
    assert expected_request1.community_id == test_community.id


def test_check_if_user_has_sent_a_request(test_client):
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

    assert not result1  # este usuario seta ya en la comunidad, por lo que es falso
    assert result2  # este usuario si que ha enviado una solicitud
    assert not result3  # este usuario no ha enviado solicitud


def test_get_all_request_sent_to_community(test_client):
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
    test_user1 = db.session.get(User, 4)
    test_user2 = db.session.get(User, 5)

    test_community = Community.query.filter_by(name="sample community").first()

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    expected_to_be_accepted_request = all_requests[0]
    join_service.accept_request(test_user1, test_community, expected_to_be_accepted_request)

    test_community = Community.query.filter_by(name="sample community").first()
    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert test_user1 in test_community.members
    assert len(all_requests) == 1
    assert all_requests[0].user_who_wants_to_join_id == test_user2.id


def test_accept_request_bad(test_client):
    test_user1 = db.session.get(User, 4)
    test_user2 = db.session.get(User, 5)

    test_community = Community.query.filter_by(name="sample community").first()

    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    expected_to_be_accepted_request = all_requests[0]
    expected_to_be_false = join_service.accept_request(test_user1, test_community, expected_to_be_accepted_request)

    test_community = Community.query.filter_by(name="sample community").first()
    all_requests = join_service.get_all_request_by_community_id(test_community.id)

    assert test_user2 not in test_community.members
    assert not expected_to_be_false
    assert len(all_requests) == 1
    assert all_requests[0].user_who_wants_to_join_id == test_user2.id


def test_decline_request(test_client):
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
