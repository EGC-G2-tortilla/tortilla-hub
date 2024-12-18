from datetime import datetime, timezone
import logging
from flask_login import current_user
from typing import Optional
from sqlalchemy import desc, func

from app.modules.dataset.models import (
    Author,
    DOIMapping,
    DSDownloadRecord,
    DSMetaData,
    DSViewRecord,
    DataSet,
    DatasetStatus,
    DatasetRating,
)
from core.repositories.BaseRepository import BaseRepository

logger = logging.getLogger(__name__)


class AuthorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Author)

    def most_popular_authors(self):
        return (
            self.model.query.join(
                DSMetaData, self.model.ds_meta_data_id == DSMetaData.id
            )
            .join(DataSet, DSMetaData.id == DataSet.ds_meta_data_id)
            .join(DSDownloadRecord, DataSet.id == DSDownloadRecord.dataset_id)
            .group_by(self.model.id)
            .order_by(desc(func.count(DSDownloadRecord.id)))
            .limit(4)
            .all()
        )

    def total_downloads_by_author(self, author_id: int):
        return (
            self.model.query.join(
                DSMetaData, self.model.ds_meta_data_id == DSMetaData.id
            )
            .join(DataSet, DSMetaData.id == DataSet.ds_meta_data_id)
            .join(DSDownloadRecord, DataSet.id == DSDownloadRecord.dataset_id)
            .filter(self.model.id == author_id)
            .count()
        )


class DSDownloadRecordRepository(BaseRepository):
    def __init__(self):
        super().__init__(DSDownloadRecord)

    def total_dataset_downloads(self) -> int:
        max_id = self.model.query.with_entities(func.max(self.model.id)).scalar()
        return max_id if max_id is not None else 0


class DSMetaDataRepository(BaseRepository):
    def __init__(self):
        super().__init__(DSMetaData)

    def filter_by_doi(self, doi: str) -> Optional[DSMetaData]:
        return self.model.query.filter_by(dataset_doi=doi).first()


class DSViewRecordRepository(BaseRepository):
    def __init__(self):
        super().__init__(DSViewRecord)

    def total_dataset_views(self) -> int:
        max_id = self.model.query.with_entities(func.max(self.model.id)).scalar()
        return max_id if max_id is not None else 0

    def the_record_exists(self, dataset: DataSet, user_cookie: str):
        return self.model.query.filter_by(
            user_id=current_user.id if current_user.is_authenticated else None,
            dataset_id=dataset.id,
            view_cookie=user_cookie,
        ).first()

    def create_new_record(self, dataset: DataSet, user_cookie: str) -> DSViewRecord:
        return self.create(
            user_id=current_user.id if current_user.is_authenticated else None,
            dataset_id=dataset.id,
            view_date=datetime.now(timezone.utc),
            view_cookie=user_cookie,
        )


class DataSetRepository(BaseRepository):
    def __init__(self):
        super().__init__(DataSet)

    def get_synchronized(self, current_user_id: int) -> DataSet:
        return (
            self.model.query.join(DSMetaData)
            .filter(
                DataSet.user_id == current_user_id, DSMetaData.dataset_doi.isnot(None)
            )
            .order_by(self.model.created_at.desc())
            .all()
        )

    def get_unsynchronized(self, current_user_id: int) -> DataSet:
        return (
            self.model.query.join(DSMetaData)
            .filter(
                DataSet.user_id == current_user_id, DSMetaData.dataset_doi.is_(None)
            )
            .order_by(self.model.created_at.desc())
            .all()
        )

    def get_unsynchronized_dataset(
        self, current_user_id: int, dataset_id: int
    ) -> DataSet:
        return (
            self.model.query.join(DSMetaData)
            .filter(
                DataSet.user_id == current_user_id,
                DataSet.id == dataset_id,
                DSMetaData.dataset_doi.is_(None),
            )
            .first()
        )

    def count_synchronized_datasets(self):
        return (
            self.model.query.join(DSMetaData)
            .filter(DSMetaData.dataset_doi.isnot(None))
            .count()
        )

    def count_unsynchronized_datasets(self):
        return (
            self.model.query.join(DSMetaData)
            .filter(DSMetaData.dataset_doi.is_(None))
            .count()
        )

    def latest_synchronized(self):
        return (
            self.model.query.join(DSMetaData)
            .filter(DSMetaData.dataset_doi.isnot(None))
            .order_by(desc(self.model.id))
            .limit(5)
            .all()
        )

    def most_downloaded(self):
        return (
            self.model.query.join(
                DSDownloadRecord, DSDownloadRecord.dataset_id == self.model.id
            )
            .group_by(self.model.id)
            .order_by(desc(func.count(DSDownloadRecord.id)))
            .limit(4)
            .all()
        )

    def get_by_community_id(self, community_id: int):
        return (
            self.model.query.join(DSMetaData)
            .filter(
                DataSet.community_id == community_id, DSMetaData.dataset_doi.isnot(None)
            )
            .all()
        )

    def get_unsynchronized_by_community_id_and_user_id(
        self, community_id: int, current_user_id: int
    ):
        return (
            self.model.query.join(DSMetaData)
            .filter(
                DataSet.community_id == community_id,
                DataSet.user_id == current_user_id,
                DSMetaData.dataset_doi.is_(None),
            )
            .all()
        )

    def get_all_datasets(self):
        return self.model.query.all()

    def get_user_staged_datasets(self, current_user_id: int):
        return (
            self.model.query.join(DSMetaData)
            .filter(
                DataSet.user_id == current_user_id,
                DSMetaData.dataset_status == DatasetStatus.STAGED,
                DSMetaData.dataset_doi.is_(None),
            )
            .all()
        )

    def get_user_unstaged_datasets(self, current_user_id: int):
        return (
            self.model.query.join(DSMetaData)
            .filter(
                DataSet.user_id == current_user_id,
                DSMetaData.dataset_status == DatasetStatus.UNSTAGED,
                DSMetaData.dataset_doi.is_(None),
            )
            .all()
        )

    def get_user_published_datasets(self, current_user_id: int):
        return (
            self.model.query.join(DSMetaData)
            .filter(
                DataSet.user_id == current_user_id,
                DSMetaData.dataset_status == DatasetStatus.PUBLISHED,
                DSMetaData.dataset_doi.isnot(None),
            )
            .all()
        )


class DOIMappingRepository(BaseRepository):
    def __init__(self):
        super().__init__(DOIMapping)

    def get_new_doi(self, old_doi: str) -> str:
        return self.model.query.filter_by(dataset_doi_old=old_doi).first()


class DatasetRatingRepository(BaseRepository):
    def __init__(self):
        super().__init__(DatasetRating)

    def get_rating_by_user_and_dataset(
        self, user_id: int, dataset_id: int
    ) -> Optional[DatasetRating]:
        """Gets the rating given by a user for a specific dataset."""
        return (
            self.session.query(DatasetRating)
            .filter_by(user_id=user_id, dataset_id=dataset_id)
            .first()
        )

    def get_average_rating(self, dataset_id: int) -> float:
        """Calculates the average rating for a dataset."""
        result = (
            self.session.query(func.avg(DatasetRating.rating))
            .filter_by(dataset_id=dataset_id)
            .scalar()
        )
        return round(result, 2) if result else 0.0

    def get_ratings_count(self, dataset_id: int) -> int:
        """Gets the total number of ratings for a dataset."""
        return (
            self.session.query(func.count(DatasetRating.id))
            .filter_by(dataset_id=dataset_id)
            .scalar()
        )

    def save(self, instance):
        """Saves an object to the database."""
        self.session.add(instance)
        self.session.commit()
