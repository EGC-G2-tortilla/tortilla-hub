import pytest

from app import db
from app.modules.auth.models import User
from app.modules.community.models import Community
from app.modules.community.services import CommunityService

service = CommunityService()


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        user_test = User(email="user@example.com", password="test1234")
        db.session.add(user_test)
        user_test2 = User(email="user_1@example.com", password="test1234")
        db.session.add(user_test2)
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
    test_user = User.query.filter_by(email="user@example.com").first()
    test_community = Community.query.filter_by(name="sample community").first()

    assert test_community.name == "sample community"
    assert test_community.url == "https://sample.com"
    assert test_community.description == "sample sample sample"
    assert test_user in test_community.members


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
