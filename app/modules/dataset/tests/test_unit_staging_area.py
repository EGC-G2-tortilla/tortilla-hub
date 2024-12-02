from app.modules.dataset.models import (
    DataSet,
    DatasetStatus,
    DSMetaData,
    PublicationType,
)
from app.modules.auth.models import User
from app.modules.conftest import login, logout
import pytest
from app import db


@pytest.fixture(scope="module")
def test_client(test_client):
    with test_client.application.app_context():
        user = User(email="user@example.com", password="test1234")
        user2 = User(email="user2@example.com", password="test1234")
        db.session.add(user)
        db.session.add(user2)
        db.session.commit()
        ds_meta_data = DSMetaData(
            title="Sample Dataset",
            description="Sample dataset description",
            publication_type=PublicationType.JOURNAL_ARTICLE,
            dataset_status=DatasetStatus.UNSTAGED,
        )
        ds_meta_data2 = DSMetaData(
            title="Sample staged dataset",
            description="Sample staged dataset description",
            publication_type=PublicationType.JOURNAL_ARTICLE,
            dataset_status=DatasetStatus.STAGED,
        )
        db.session.add(ds_meta_data)
        db.session.add(ds_meta_data2)
        data_set = DataSet(user_id=user.id, ds_meta_data_id=ds_meta_data.id)
        data_set2 = DataSet(user_id=user.id, ds_meta_data_id=ds_meta_data2.id)
        db.session.add(data_set)
        db.session.add(data_set2)
        db.session.commit()
    yield test_client


def test_fail_to_stage_dataset(test_client):
    """
    Test that a dataset cannot be set to staged if the user does not own the dataset
    """
    login_response = login(test_client, "user2@example.com", "test1234")
    user = db.session.get(User, 3)
    assert user.email == "user2@example.com"
    assert login_response.status_code == 200
    dataset = db.session.get(DataSet, 1)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.UNSTAGED
    response = test_client.post(f"/dataset/stage/{dataset.id}")
    # Check that the response is a 403 error
    assert response.status_code == 403
    # Check that the dataset status has not been updated
    dataset = db.session.get(DataSet, 1)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.UNSTAGED
    logout(test_client)


def test_fail_to_stage_dataset_unstaged(test_client):
    """
    Test that a dataset cannot be set to staged if it is already staged
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200
    # Check that the dataset is already staged
    dataset = db.session.get(DataSet, 2)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.STAGED
    response = test_client.post(f"/dataset/stage/{dataset.id}")
    # Check that the response is a 500 error
    assert response.status_code == 500
    # Check that the dataset status has not been updated
    dataset = db.session.get(DataSet, 2)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.STAGED
    logout(test_client)


def test_set_dataset_to_staged(test_client):
    """
    Test that a dataset can be set to staged
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200
    dataset = db.session.get(DataSet, 1)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.UNSTAGED
    response = test_client.post(f"/dataset/stage/{dataset.id}")
    # Check that the response is a redirect
    assert response.status_code == 302
    # Check that the dataset status has been updated
    dataset = db.session.get(DataSet, 1)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.STAGED
    # Check that a flash message has been set
    with test_client.session_transaction() as session:
        flash_messages = session["_flashes"]
        assert any(
            "Dataset staged successfully" in message
            for category, message in flash_messages
        )
    # Check that the user is redirected to the dataset page
    assert response.location == "/dataset/list"
    logout(test_client)


def test_set_dataset_to_unstaged(test_client):
    """
    Test that a dataset can be set to unstaged
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200
    # Check that the dataset is already staged
    dataset = db.session.get(DataSet, 2)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.STAGED
    response = test_client.post(f"/dataset/unstage/{dataset.id}")
    # Check that the response is a redirect
    assert response.status_code == 302
    # Check that the dataset status has been updated
    dataset = db.session.get(DataSet, 2)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.UNSTAGED
    # Check that a flash message has been set
    with test_client.session_transaction() as session:
        flash_messages = session["_flashes"]
        assert any(
            "Dataset unstaged successfully" in message
            for category, message in flash_messages
        )
    # Check that the user is redirected to the dataset page
    assert response.location == "/dataset/list"
    logout(test_client)


def test_fail_to_unstage_dataset(test_client):
    """
    Test that a dataset cannot be set to unstaged if the user does not own the dataset
    """
    login_response = login(test_client, "user2@example.com", "test1234")
    assert login_response.status_code == 200
    # Check that the dataset is already staged
    dataset = db.session.get(DataSet, 1)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.STAGED
    response = test_client.post(f"/dataset/unstage/{dataset.id}")
    # Check that the response is a 403 error
    assert response.status_code == 403
    # Check that the dataset status has not been updated
    dataset = db.session.get(DataSet, 1)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.STAGED
    logout(test_client)


def test_fail_to_unstage_dataset_unstaged(test_client):
    """
    Test that a dataset cannot be set to unstaged if it is already unstaged
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200
    # Check that the dataset is already unstaged
    dataset = db.session.get(DataSet, 2)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.UNSTAGED
    response = test_client.post(f"/dataset/unstage/{dataset.id}")
    # Check that the response is a 500 error
    assert response.status_code == 500
    # Check that the dataset status has not been updated
    dataset = db.session.get(DataSet, 2)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.UNSTAGED
    logout(test_client)


def test_publish_all_datasets(test_client):
    """
    Test that all datasets can be published
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200
    # Check that the datasets are not published
    dataset = db.session.get(DataSet, 1)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.STAGED
    dataset = db.session.get(DataSet, 2)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.UNSTAGED
    response = test_client.post("/dataset/publish")
    # Check that the response is a redirect
    assert response.status_code == 302
    # Check that the datasets have been updated correctly
    dataset = db.session.get(DataSet, 1)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.PUBLISHED
    dataset = db.session.get(DataSet, 2)
    assert dataset.ds_meta_data.dataset_status == DatasetStatus.UNSTAGED
    logout(test_client)
