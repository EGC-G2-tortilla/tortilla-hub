import pytest
from app import db
from app.modules.dataset.models import (
    Author,
    DataSet,
    DSDownloadRecord,
    DSMetaData,
    DSMetrics,
    PublicationType,
)
from app.modules.auth.models import User
from app.modules.dataset.repositories import AuthorRepository, DataSetRepository

author_repo = AuthorRepository()
dataset_repo = DataSetRepository()


# -------------- FIXTURES --------------


@pytest.fixture(scope="module")
def test_client(test_client):
    with test_client.application.app_context():
        # Crear datos de prueba
        user1 = User(email="user1@example.com", password="test1234")
        user2 = User(email="user2@example.com", password="test1234")
        user3 = User(email="user3@example.com", password="test1234")
        user4 = User(email="user4@example.com", password="test1234")
        user5 = User(email="user5@example.com", password="test1234")
        db.session.add_all([user1, user2, user3, user4, user5])
        db.session.commit()

        ds_metrics1 = DSMetrics(number_of_models="10", number_of_features="100")
        ds_metrics2 = DSMetrics(number_of_models="30", number_of_features="200")
        ds_metrics3 = DSMetrics(number_of_models="30", number_of_features="200")
        ds_metrics4 = DSMetrics(number_of_models="30", number_of_features="200")
        ds_metrics5 = DSMetrics(number_of_models="1", number_of_features="10")
        db.session.add_all(
            [ds_metrics1, ds_metrics2, ds_metrics3, ds_metrics4, ds_metrics5]
        )
        db.session.commit()

        ds_meta1 = DSMetaData(
            title="Dataset 1",
            dataset_doi="doi1",
            ds_metrics_id=ds_metrics1.id,
            description="description1...",
            publication_type=PublicationType.BOOK,
        )
        ds_meta2 = DSMetaData(
            title="Dataset 2",
            dataset_doi="doi2",
            ds_metrics_id=ds_metrics2.id,
            description="description2...",
            publication_type=PublicationType.BOOK,
        )
        ds_meta3 = DSMetaData(
            title="Dataset 3",
            dataset_doi="doi3",
            ds_metrics_id=ds_metrics3.id,
            description="description3...",
            publication_type=PublicationType.REPORT,
        )
        ds_meta4 = DSMetaData(
            title="Dataset 4",
            dataset_doi="doi4",
            ds_metrics_id=ds_metrics4.id,
            description="description4...",
            publication_type=PublicationType.BOOK,
        )
        ds_meta5 = DSMetaData(
            title="Dataset 5",
            dataset_doi="doi5",
            ds_metrics_id=ds_metrics5.id,
            description="description5...",
            publication_type=PublicationType.BOOK,
        )
        db.session.add_all([ds_meta1, ds_meta2, ds_meta3, ds_meta4, ds_meta5])
        db.session.commit()

        author1 = Author(name="Author 1", ds_meta_data_id=ds_meta1.id)
        author2 = Author(name="Author 2", ds_meta_data_id=ds_meta2.id)
        author3 = Author(name="Author 3", ds_meta_data_id=ds_meta3.id)
        author4 = Author(name="Author 4", ds_meta_data_id=ds_meta4.id)
        author5 = Author(name="Author 5", ds_meta_data_id=ds_meta5.id)
        db.session.add_all([author1, author2, author3, author4, author5])
        db.session.commit()

        dataset1 = DataSet(user_id=user1.id, ds_meta_data_id=ds_meta1.id)
        dataset2 = DataSet(user_id=user2.id, ds_meta_data_id=ds_meta2.id)
        dataset3 = DataSet(user_id=user3.id, ds_meta_data_id=ds_meta3.id)
        dataset4 = DataSet(user_id=user4.id, ds_meta_data_id=ds_meta4.id)
        dataset5 = DataSet(user_id=user5.id, ds_meta_data_id=ds_meta5.id)
        db.session.add_all([dataset1, dataset2, dataset3, dataset4, dataset5])
        db.session.commit()

        download_record1 = DSDownloadRecord(
            dataset_id=dataset1.id, download_cookie="cookie1"
        )
        download_record2 = DSDownloadRecord(
            dataset_id=dataset2.id, download_cookie="cookie2"
        )
        download_record3 = DSDownloadRecord(
            dataset_id=dataset3.id, download_cookie="cookie3"
        )
        download_record4 = DSDownloadRecord(
            dataset_id=dataset4.id, download_cookie="cookie4"
        )
        download_record5 = DSDownloadRecord(
            dataset_id=dataset5.id, download_cookie="cookie5"
        )
        download_record6 = DSDownloadRecord(
            dataset_id=dataset1.id, download_cookie="cookie6"
        )
        download_record7 = DSDownloadRecord(
            dataset_id=dataset1.id, download_cookie="cookie7"
        )
        download_record8 = DSDownloadRecord(
            dataset_id=dataset2.id, download_cookie="cookie8"
        )
        download_record9 = DSDownloadRecord(
            dataset_id=dataset3.id, download_cookie="cookie9"
        )
        download_record10 = DSDownloadRecord(
            dataset_id=dataset4.id, download_cookie="cookie10"
        )
        db.session.add_all(
            [
                download_record1,
                download_record2,
                download_record3,
                download_record4,
                download_record5,
                download_record6,
                download_record7,
                download_record8,
                download_record9,
                download_record10,
            ]
        )
        db.session.commit()

    yield test_client


# -------------- TESTS DE REPOSITORIO --------------


def test_most_popular_authors(test_client):
    with test_client.application.app_context():
        popular_authors = author_repo.most_popular_authors()
        assert len(popular_authors) == 4
        assert all(
            author.name in ["Author 1", "Author 2", "Author 3", "Author 4"]
            for author in popular_authors
        )
        print([author.name for author in popular_authors])


def test_most_popular_authors_negative(test_client):
    with test_client.application.app_context():
        # Eliminar registros de descarga para Author 5
        DSDownloadRecord.query.filter_by(dataset_id=5).delete()
        db.session.commit()

        # Verificar que Author 5 no está entre los populares
        popular_authors = author_repo.most_popular_authors()
        assert "Author 5" not in [author.name for author in popular_authors]
        print([author.name for author in popular_authors])


def test_most_downloaded(test_client):
    with test_client.application.app_context():
        most_downloaded_datasets = dataset_repo.most_downloaded()
        assert len(most_downloaded_datasets) == 4


def test_most_downloaded_negative(test_client):
    with test_client.application.app_context():
        most_downloaded_datasets = dataset_repo.most_downloaded()
        assert not any(
            dataset.ds_meta_data.title == "Dataset 5"
            for dataset in most_downloaded_datasets
        )


def test_latest_synchronized(test_client):
    with test_client.application.app_context():
        latest_datasets = dataset_repo.latest_synchronized()
        assert len(latest_datasets) == 5


def test_latest_synchronized_negative(test_client):
    with test_client.application.app_context():
        latest_datasets = dataset_repo.latest_synchronized()
        assert not any(
            dataset.ds_meta_data.title == "Dataset 1"
            for dataset in latest_datasets
            if dataset.id < 0
        )


# -------------- TESTS DE SERVICIO --------------


def test_service_most_popular_authors(test_client):
    with test_client.application.app_context():
        popular_authors = author_repo.most_popular_authors()
        assert len(popular_authors) == 4
        assert all(
            author.name in ["Author 1", "Author 2", "Author 3", "Author 4"]
            for author in popular_authors
        )
        print([author.name for author in popular_authors])


def test_service_most_popular_authors_negative(test_client):
    with test_client.application.app_context():
        DSDownloadRecord.query.filter_by(dataset_id=5).delete()
        db.session.commit()

        popular_authors = author_repo.most_popular_authors()
        assert "Author 5" not in [author.name for author in popular_authors]
        print([author.name for author in popular_authors])


def test_service_most_downloaded(test_client):
    with test_client.application.app_context():
        most_downloaded_datasets = dataset_repo.most_downloaded()
        assert len(most_downloaded_datasets) == 4


def test_service_most_downloaded_negative(test_client):
    with test_client.application.app_context():
        most_downloaded_datasets = dataset_repo.most_downloaded()
        assert not any(
            dataset.ds_meta_data.title == "Dataset 5"
            for dataset in most_downloaded_datasets
        )


def test_service_latest_synchronized(test_client):
    with test_client.application.app_context():
        latest_datasets = dataset_repo.latest_synchronized()
        assert len(latest_datasets) == 5


def test_service_latest_synchronized_negative(test_client):
    with test_client.application.app_context():
        latest_datasets = dataset_repo.latest_synchronized()
        assert not any(
            dataset.ds_meta_data.title == "Dataset 1"
            for dataset in latest_datasets
            if dataset.id < 0
        )
