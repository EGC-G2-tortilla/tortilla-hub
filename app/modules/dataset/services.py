import base64
import logging
import os
import hashlib
import shutil
from typing import Optional
import uuid

from flask import request, session
from sqlalchemy import func
import requests

from app.modules.auth.services import AuthenticationService
from app.modules.dataset.models import (
    DSDownloadRecord,
    DSViewRecord,
    DataSet,
    DSMetaData,
    DatasetStatus,
)
from app.modules.dataset.repositories import (
    AuthorRepository,
    DOIMappingRepository,
    DSDownloadRecordRepository,
    DSMetaDataRepository,
    DSViewRecordRepository,
    DataSetRepository,
    DatasetRatingRepository,
)
from app.modules.featuremodel.repositories import (
    FMMetaDataRepository,
    FeatureModelRepository,
)
from app.modules.hubfile.repositories import (
    HubfileDownloadRecordRepository,
    HubfileRepository,
    HubfileViewRecordRepository,
)
from core.services.BaseService import BaseService
from app.modules.fakenodo.services import FakenodoService

fakenodo = FakenodoService()
logger = logging.getLogger(__name__)


def calculate_checksum_and_size(file_path):
    file_size = os.path.getsize(file_path)
    with open(file_path, "rb") as file:
        content = file.read()
        hash_md5 = hashlib.md5(content).hexdigest()
        return hash_md5, file_size


class DataSetService(BaseService):
    def __init__(self):
        super().__init__(DataSetRepository())
        self.feature_model_repository = FeatureModelRepository()
        self.author_repository = AuthorRepository()
        self.dsmetadata_repository = DSMetaDataRepository()
        self.fmmetadata_repository = FMMetaDataRepository()
        self.dsdownloadrecord_repository = DSDownloadRecordRepository()
        self.hubfiledownloadrecord_repository = HubfileDownloadRecordRepository()
        self.hubfilerepository = HubfileRepository()
        self.dsviewrecord_repostory = DSViewRecordRepository()
        self.hubfileviewrecord_repository = HubfileViewRecordRepository()

    def move_feature_models(self, dataset: DataSet):
        current_user = AuthenticationService().get_authenticated_user()
        source_dir = current_user.temp_folder()

        working_dir = os.getenv("WORKING_DIR", "")
        dest_dir = os.path.join(
            working_dir, "uploads", f"user_{current_user.id}", f"dataset_{dataset.id}"
        )
        dest_dir = os.path.join(
            working_dir, "uploads", f"user_{current_user.id}", f"dataset_{dataset.id}"
        )

        os.makedirs(dest_dir, exist_ok=True)

        for feature_model in dataset.feature_models:
            uvl_filename = feature_model.fm_meta_data.uvl_filename
            shutil.move(os.path.join(source_dir, uvl_filename), dest_dir)

    def get_synchronized(self, current_user_id: int) -> DataSet:
        return self.repository.get_synchronized(current_user_id)

    def get_unsynchronized(self, current_user_id: int) -> DataSet:
        return self.repository.get_unsynchronized(current_user_id)

    def get_unsynchronized_dataset(
        self, current_user_id: int, dataset_id: int
    ) -> DataSet:
        return self.repository.get_unsynchronized_dataset(current_user_id, dataset_id)

    def latest_synchronized(self):
        return self.repository.latest_synchronized()

    def most_downloaded(self):
        downloaded_datasets = self.repository.most_downloaded()
        result = []

        for dataset in downloaded_datasets:
            download_count = (
                self.repository.session.query(func.count(DSDownloadRecord.id))
                .filter(DSDownloadRecord.dataset_id == dataset.id)
                .scalar()
            )
            result.append({"name": dataset.name(), "downloads": download_count})

        return result

    def count_synchronized_datasets(self):
        return self.repository.count_synchronized_datasets()

    def count_feature_models(self):
        return self.feature_model_service.count_feature_models()

    def count_authors(self) -> int:
        return self.author_repository.count()

    def count_dsmetadata(self) -> int:
        return self.dsmetadata_repository.count()

    def total_dataset_downloads(self) -> int:
        return self.dsdownloadrecord_repository.total_dataset_downloads()

    def total_dataset_views(self) -> int:
        return self.dsviewrecord_repostory.total_dataset_views()

    def upload_to_hub(self, hub, owner_repo, file_path):
        file_name = file_path.split("/")[-1]

        if hub == "github":
            base_url = f"https://api.github.com/repos/{owner_repo}/contents/uvlmodels/{file_name}"
            token = session["github_token"]

            headers = {
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github.v3+json",
            }
            sha = None
            response = requests.get(base_url, headers=headers, timeout=10)
            if response.status_code == 200:
                sha = response.json().get("sha")

            with open(file_path, "rb") as file:
                content = file.read()
            content_base64 = base64.b64encode(content).decode("utf-8")

            data = {
                "message": "Subiendo modelo uvl desde uvlhub",
                "content": content_base64,
                "branch": "main",
            }
            if sha:
                data["sha"] = sha  # Agregar el SHA si el archivo ya existe

            # Subir el archivo
            response = requests.put(base_url, json=data, headers=headers, timeout=10)
            return logger.info(
                f"Subida a GitHub del archivo {file_name}: {response.status_code} {response.reason}"
            )

        elif hub == "gitlab":
            base_url = (
                f"https://gitlab.com/api/v4/projects/{owner_repo}/repository/commits"
            )
            token = session["gitlab_token"]

            with open(file_path, "rb") as file:
                content = file.read()
            content_base64 = base64.b64encode(content).decode("utf-8")

            data = {
                "branch": "main",
                "commit_message": "Subiendo modelo uvl desde uvlhub",
                "actions": [
                    {
                        "action": "create",
                        "file_path": f"uvlmodels/{file_name}",
                        "content": content_base64,
                        "encoding": "base64",
                    }
                ],
            }

            headers = {"Authorization": f"Bearer {token}"}

            response = requests.post(base_url, json=data, headers=headers, timeout=10)
            if response.status_code == 400:  # Error si el archivo ya existe
                data["actions"][0]["action"] = "update"
                response = requests.post(
                    base_url, json=data, headers=headers, timeout=10
                )

            return logger.info(
                f"Subida a GitLab del archivo {file_name}: {response.status_code} {response.reason}"
            )

    def create_from_form(self, form, current_user, community=None) -> DataSet:
        main_author = {
            "name": f"{current_user.profile.surname}, {current_user.profile.name}",
            "affiliation": current_user.profile.affiliation,
            "orcid": current_user.profile.orcid,
        }
        github_repo = form.github_repo.data
        gitlab_repo = form.gitlab_repo.data
        try:
            logger.info(f"Creating dsmetadata...: {form.get_dsmetadata()}")
            dsmetadata = self.dsmetadata_repository.create(**form.get_dsmetadata())
            for author_data in [main_author] + form.get_authors():
                author = self.author_repository.create(
                    commit=False, ds_meta_data_id=dsmetadata.id, **author_data
                )
                dsmetadata.authors.append(author)

            if community is not None:
                dataset = self.create(
                    commit=False,
                    user_id=current_user.id,
                    ds_meta_data_id=dsmetadata.id,
                    community_id=community.id,
                )
                print("\n\tcommunity is not none\n")
            else:
                dataset = self.create(
                    commit=False, user_id=current_user.id, ds_meta_data_id=dsmetadata.id
                )
                print("\n\tcommunity is none\n")

            for feature_model in form.feature_models:
                uvl_filename = feature_model.uvl_filename.data
                fmmetadata = self.fmmetadata_repository.create(
                    commit=False, **feature_model.get_fmmetadata()
                )
                for author_data in feature_model.get_authors():
                    author = self.author_repository.create(
                        commit=False, fm_meta_data_id=fmmetadata.id, **author_data
                    )
                    fmmetadata.authors.append(author)

                fm = self.feature_model_repository.create(
                    commit=False, data_set_id=dataset.id, fm_meta_data_id=fmmetadata.id
                )

                # associated files in feature model
                file_path = os.path.join(current_user.temp_folder(), uvl_filename)
                checksum, size = calculate_checksum_and_size(file_path)

                file = self.hubfilerepository.create(
                    commit=False,
                    name=uvl_filename,
                    checksum=checksum,
                    size=size,
                    feature_model_id=fm.id,
                )
                fm.files.append(file)
                if github_repo:
                    self.upload_to_hub("github", github_repo, file_path)
                if gitlab_repo:
                    self.upload_to_hub("gitlab", gitlab_repo, file_path)

            self.repository.session.commit()
        except Exception as exc:
            logger.info(f"Exception creating dataset from form...: {exc}")
            self.repository.session.rollback()
            raise exc
        return dataset

    def update_dsmetadata(self, id, **kwargs):
        return self.dsmetadata_repository.update(id, **kwargs)

    def get_uvlhub_doi(self, dataset: DataSet) -> str:
        domain = os.getenv("DOMAIN", "localhost")
        return f"http://{domain}/doi/{dataset.ds_meta_data.dataset_doi}"

    def get_by_community_id(self, community_id: int):
        return self.repository.get_by_community_id(community_id)

    def get_all_datasets(self):
        return self.repository.get_all_datasets()

    def get_dataset_by_id(self, dataset_id):
        return self.repository.get_or_404(dataset_id)

    def set_dataset_to_staged(self, dataset_id):
        try:
            dataset = self.repository.get_by_id(dataset_id)
            if dataset.ds_meta_data.dataset_status == DatasetStatus.UNSTAGED:
                dataset.ds_meta_data.dataset_status = DatasetStatus.STAGED
                self.repository.session.commit()
                return dataset
            else:
                raise ValueError("Dataset is not in 'UNSTAGED' status")
        except Exception as exc:
            logger.error(f"Exception setting dataset to staged: {exc}")
            self.repository.session.rollback()
            raise exc

    def set_dataset_to_unstaged(self, dataset_id):
        try:
            dataset = self.repository.get_by_id(dataset_id)
            if dataset.ds_meta_data.dataset_status == DatasetStatus.STAGED:
                dataset.ds_meta_data.dataset_status = DatasetStatus.UNSTAGED
                self.repository.session.commit()
                return dataset
            else:
                raise ValueError("Dataset is not in 'STAGED' status")
        except Exception as exc:
            logger.error(f"Exception setting dataset to unstaged: {exc}")
            self.repository.session.rollback()
            raise exc

    def publish_datasets(self, current_user_id):
        try:
            datasets = self.repository.get_user_staged_datasets(current_user_id)
            for dataset in datasets:
                if dataset.ds_meta_data.dataset_status == DatasetStatus.STAGED:
                    fakenodo.test_full_connection()
                    dataset.ds_meta_data.dataset_status = DatasetStatus.PUBLISHED
                    self.repository.session.commit()
                else:
                    raise ValueError("Dataset is not in 'STAGED' status")
        except Exception as exc:
            logger.error(f"Exception setting dataset to published: {exc}")
            self.repository.session.rollback()

    def stage_all_datasets(self, current_user_id):
        try:

            datasets = self.repository.get_user_unstaged_datasets(current_user_id)
            if len(datasets) > 0:
                for dataset in datasets:
                    dataset.ds_meta_data.dataset_status = DatasetStatus.STAGED
                    self.repository.session.commit()
            else:
                raise ValueError("There's no datasets available to stage")
        except Exception as exc:
            logger.error(f"Exception setting dataset to staged: {exc}")
            self.repository.session.rollback()


class AuthorService(BaseService):
    def __init__(self):
        super().__init__(AuthorRepository())

    def most_popular_authors(self):
        popular_authors = self.repository.most_popular_authors()
        result = []

        for author in popular_authors:
            download_count = self.repository.total_downloads_by_author(author.id)
            result.append({"name": author.name, "downloads": download_count})

        return result


class DSDownloadRecordService(BaseService):
    def __init__(self):
        super().__init__(DSDownloadRecordRepository())


class DSMetaDataService(BaseService):
    def __init__(self):
        super().__init__(DSMetaDataRepository())

    def update(self, id, **kwargs):
        return self.repository.update(id, **kwargs)

    def filter_by_doi(self, doi: str) -> Optional[DSMetaData]:
        return self.repository.filter_by_doi(doi)


class DSViewRecordService(BaseService):
    def __init__(self):
        super().__init__(DSViewRecordRepository())

    def the_record_exists(self, dataset: DataSet, user_cookie: str):
        return self.repository.the_record_exists(dataset, user_cookie)

    def create_new_record(self, dataset: DataSet, user_cookie: str) -> DSViewRecord:
        return self.repository.create_new_record(dataset, user_cookie)

    def create_cookie(self, dataset: DataSet) -> str:

        user_cookie = request.cookies.get("view_cookie")
        if not user_cookie:
            user_cookie = str(uuid.uuid4())

        existing_record = self.the_record_exists(
            dataset=dataset, user_cookie=user_cookie
        )

        if not existing_record:
            self.create_new_record(dataset=dataset, user_cookie=user_cookie)

        return user_cookie


class DOIMappingService(BaseService):
    def __init__(self):
        super().__init__(DOIMappingRepository())

    def get_new_doi(self, old_doi: str) -> str:
        doi_mapping = self.repository.get_new_doi(old_doi)
        if doi_mapping:
            return doi_mapping.dataset_doi_new
        else:
            return None


class SizeService:

    def __init__(self):
        pass

    def get_human_readable_size(self, size: int) -> str:
        if size < 1024:
            return f"{size} bytes"
        elif size < 1024**2:
            return f"{round(size / 1024, 2)} KB"
        elif size < 1024**3:
            return f"{round(size / (1024 ** 2), 2)} MB"
        else:
            return f"{round(size / (1024 ** 3), 2)} GB"


class DatasetRatingService(BaseService):
    def __init__(self):
        super().__init__(DatasetRatingRepository())

    def rate_dataset(self, user_id: int, dataset_id: int, rating_value: int):
        """Allows registering or updating a rating for a dataset."""
        try:
            rating_value = int(rating_value)
        except ValueError:
            raise ValueError("Rating value must be an integer")

        if not (1 <= rating_value <= 5):
            raise ValueError("Rating value must be between 1 and 5")

        # Check if a previous rating exists
        existing_rating = self.repository.get_rating_by_user_and_dataset(
            user_id, dataset_id
        )
        if existing_rating:
            # Update the existing rating
            existing_rating.rating = rating_value
            self.repository.save(existing_rating)
        else:
            # Create a new rating
            self.repository.create(
                user_id=user_id, dataset_id=dataset_id, rating=rating_value
            )

    def get_dataset_rating_summary(self, dataset_id: int):
        """Gets the average and total number of ratings for a dataset."""
        average_rating = self.repository.get_average_rating(dataset_id)
        total_ratings = self.repository.get_ratings_count(dataset_id)
        return {"average_rating": average_rating, "total_ratings": total_ratings}

    def get_user_rating(self, user_id: int, dataset_id: int) -> Optional[int]:
        """Gets the rating given by a user for a specific dataset."""
        rating = self.repository.get_rating_by_user_and_dataset(user_id, dataset_id)
        return rating.rating if rating else None
