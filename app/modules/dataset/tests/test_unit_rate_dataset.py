import pytest
from app import db
from app.modules.auth.models import User
from app.modules.dataset.models import (
    DatasetRating,
    DataSet,
    DSMetrics,
    DSMetaData,
    PublicationType,
)
from app.modules.dataset.repositories import DatasetRatingRepository
from app.modules.dataset.services import DatasetRatingService

from sqlalchemy.orm import joinedload

rating_repository = DatasetRatingRepository()
rating_service = DatasetRatingService()


@pytest.fixture(scope="module")
def test_client_with_ratings(test_client):
    """Fixture to set up test data for ratings."""
    with test_client.application.app_context():
        # Create test users
        user1 = User(email="user1@example.com", password="test1234")
        user2 = User(email="user2@example.com", password="test1234")
        db.session.add_all([user1, user2])
        db.session.commit()

        # Create metrics
        ds_metrics1 = DSMetrics(number_of_models="10", number_of_features="100")
        ds_metrics2 = DSMetrics(number_of_models="30", number_of_features="200")
        db.session.add_all([ds_metrics1, ds_metrics2])
        db.session.commit()

        # Create metadata
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
            publication_type=PublicationType.REPORT,
        )
        db.session.add_all([ds_meta1, ds_meta2])
        db.session.commit()

        # Link metadata to datasets
        dataset1 = DataSet(user_id=user1.id, ds_meta_data_id=ds_meta1.id)
        dataset2 = DataSet(user_id=user2.id, ds_meta_data_id=ds_meta2.id)
        db.session.add_all([dataset1, dataset2])
        db.session.commit()

        # Add initial ratings
        rating1 = DatasetRating(user_id=user1.id, dataset_id=dataset1.id, rating=4)
        rating2 = DatasetRating(user_id=user2.id, dataset_id=dataset1.id, rating=5)
        db.session.add_all([rating1, rating2])
        db.session.commit()

    yield test_client


class TestRateDatasets:
    def test_rate_dataset_new(self, test_client_with_ratings):
        """Test adding a new rating."""
        with test_client_with_ratings.application.app_context():
            # Fetch user and dataset
            user_id = User.query.filter_by(email="user1@example.com").first().id
            dataset = (
                DataSet.query.options(joinedload(DataSet.ds_meta_data))
                .join(DSMetaData)
                .filter(DSMetaData.title == "Dataset 2")
                .first()
            )
            assert dataset is not None, "Dataset with title 'Dataset 2' not found."
            dataset_id = dataset.id

            # Add a new rating
            rating_service.rate_dataset(user_id, dataset_id, 3)
            new_rating = rating_repository.get_rating_by_user_and_dataset(
                user_id, dataset_id
            )

            # Validate the rating
            assert new_rating is not None
            assert new_rating.rating == 3

    def test_rate_dataset_update(self, test_client_with_ratings):
        """Test updating an existing rating."""
        with test_client_with_ratings.application.app_context():
            # Fetch user and dataset
            user_id = User.query.filter_by(email="user1@example.com").first().id
            dataset = (
                DataSet.query.options(joinedload(DataSet.ds_meta_data))
                .join(DSMetaData)
                .filter(DSMetaData.title == "Dataset 1")
                .first()
            )
            assert dataset is not None, "Dataset with title 'Dataset 1' not found."
            dataset_id = dataset.id

            # Update the existing rating
            rating_service.rate_dataset(user_id, dataset_id, 2)
            updated_rating = rating_repository.get_rating_by_user_and_dataset(
                user_id, dataset_id
            )

            # Validate the updated rating
            assert updated_rating is not None, "Rating was not found."
            assert (
                updated_rating.rating == 2
            ), "The rating value did not update correctly."

    def test_rate_dataset_invalid_type(self, test_client_with_ratings):
        """Test handling non-integer rating values."""
        with test_client_with_ratings.application.app_context():
            # Fetch user and dataset
            user_id = User.query.filter_by(email="user1@example.com").first().id
            dataset = (
                DataSet.query.options(joinedload(DataSet.ds_meta_data))
                .join(DSMetaData)
                .filter(DSMetaData.title == "Dataset 1")
                .first()
            )
            assert dataset is not None, "Dataset with title 'Dataset 1' not found."
            dataset_id = dataset.id

            # Attempt to rate with a non-integer value
            invalid_ratings = ["five", 4.5, None, {}, []]  # Different invalid types

            for invalid_rating in invalid_ratings:
                with pytest.raises(ValueError, match="Rating value must be an integer"):
                    rating_service.rate_dataset(user_id, dataset_id, invalid_rating)

    def test_rate_dataset_invalid(self, test_client_with_ratings):
        """Test handling invalid rating values."""
        with test_client_with_ratings.application.app_context():
            # Fetch user and dataset
            user_id = User.query.filter_by(email="user1@example.com").first().id
            dataset = (
                DataSet.query.options(joinedload(DataSet.ds_meta_data))
                .join(DSMetaData)
                .filter(DSMetaData.title == "Dataset 1")
                .first()
            )
            assert dataset is not None, "Dataset with title 'Dataset 1' not found."
            dataset_id = dataset.id

            # Attempt to rate with an invalid value
            with pytest.raises(ValueError):
                rating_service.rate_dataset(user_id, dataset_id, 6)

    def test_get_dataset_rating_summary(self, test_client_with_ratings):
        """Test retrieving a dataset's rating summary."""
        with test_client_with_ratings.application.app_context():
            # Fetch dataset
            dataset = (
                DataSet.query.options(joinedload(DataSet.ds_meta_data))
                .join(DSMetaData)
                .filter(DSMetaData.title == "Dataset 1")
                .first()
            )
            assert dataset is not None, "Dataset with title 'Dataset 1' not found."
            dataset_id = dataset.id

            # Retrieve the rating summary
            summary = rating_service.get_dataset_rating_summary(dataset_id)

            # Validate the rating summary
            assert (
                summary["average_rating"] == 3.5
            ), "Average rating does not match expected value."
            assert (
                summary["total_ratings"] == 2
            ), "Total ratings count does not match expected value."

    def test_get_user_rating(self, test_client_with_ratings):
        """Test retrieving a user's rating for a dataset."""
        with test_client_with_ratings.application.app_context():
            # Fetch the user ID from the database based on email
            user_id = User.query.filter_by(email="user1@example.com").first().id

            # Fetch the dataset based on the dataset's title (considering changes made)
            dataset = (
                DataSet.query.options(joinedload(DataSet.ds_meta_data))
                .join(DSMetaData)
                .filter(DSMetaData.title == "Dataset 1")
                .first()
            )
            assert dataset is not None, "Dataset with title 'Dataset 1' not found."
            dataset_id = dataset.id

            # Get the user's rating for the dataset
            user_rating = rating_service.get_user_rating(user_id, dataset_id)

            assert user_rating == 2  # Based on the initial setup
