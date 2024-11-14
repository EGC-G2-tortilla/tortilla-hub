import pytest
import uuid

from app import db
from app.modules.dataset.models import Author, DataSet, DSMetaData, DSDownloadRecord, DatasetStatus, PublicationType
from app.modules.dataset.repositories import AuthorRepository, DataSetRepository

author_repository = AuthorRepository()
dataset_repository = DataSetRepository()


@pytest.fixture(scope='module')
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        # Crear autores
        author1 = Author(name='Author 1', affiliation='Affiliation 1', orcid='0000-0000-0000-0001')
        author2 = Author(name='Author 2', affiliation='Affiliation 2', orcid='0000-0000-0000-0002')
        db.session.add(author1)
        db.session.add(author2)
        db.session.commit()

        # Crear metadatos de datasets
        ds_meta_data1 = DSMetaData(title='Dataset 1', description='Description 1',
                                   publication_type=PublicationType.DATA_MANAGEMENT_PLAN,
                                   dataset_status=DatasetStatus.PUBLISHED)
        ds_meta_data2 = DSMetaData(title='Dataset 2', description='Description 2',
                                   publication_type=PublicationType.DATA_MANAGEMENT_PLAN,
                                   dataset_status=DatasetStatus.PUBLISHED)
        db.session.add(ds_meta_data1)
        db.session.add(ds_meta_data2)
        db.session.commit()

        # Asociar autores a metadatos de datasets
        author1.ds_meta_data_id = ds_meta_data1.id
        author2.ds_meta_data_id = ds_meta_data2.id
        db.session.commit()

        # Crear datasets
        dataset1 = DataSet(user_id=1, ds_meta_data_id=ds_meta_data1.id)
        dataset2 = DataSet(user_id=1, ds_meta_data_id=ds_meta_data2.id)
        db.session.add(dataset1)
        db.session.add(dataset2)
        db.session.commit()

        # Crear registros de descargas
        download_record1 = DSDownloadRecord(user_id=1, dataset_id=dataset1.id, download_cookie=str(uuid.uuid4()))
        download_record2 = DSDownloadRecord(user_id=1, dataset_id=dataset2.id, download_cookie=str(uuid.uuid4()))
        db.session.add(download_record1)
        db.session.add(download_record2)
        db.session.commit()

    yield test_client


def test_most_popular_authors(test_client):
    """
    Test to verify that the most_popular_authors method returns the correct authors.
    """
    popular_authors = author_repository.most_popular_authors()
    assert len(popular_authors) == 2
    assert popular_authors[0].name == 'Author 1'
    assert popular_authors[1].name == 'Author 2'


def test_most_downloaded(test_client):
    """
    Test to verify that the most_downloaded method returns the correct datasets.
    """
    most_downloaded_datasets = dataset_repository.most_downloaded()
    assert len(most_downloaded_datasets) == 2
    assert most_downloaded_datasets[0].ds_meta_data.title == 'Dataset 1'
    assert most_downloaded_datasets[1].ds_meta_data.title == 'Dataset 2'
