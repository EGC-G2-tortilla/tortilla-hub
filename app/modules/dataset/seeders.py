import os
import shutil
from app.modules.auth.models import User
from app.modules.featuremodel.models import FMMetaData, FeatureModel
from app.modules.hubfile.models import Hubfile
from core.seeders.BaseSeeder import BaseSeeder
from app.modules.dataset.models import (
    DataSet,
    DSMetaData,
    PublicationType,
    DatasetStatus,
    DSMetrics,
    Author,
    DatasetRating,
)
from datetime import datetime, timezone
from dotenv import load_dotenv


class DataSetSeeder(BaseSeeder):

    priority = 2  # Lower priority

    def run(self):
        # Retrieve users
        user1 = User.query.filter_by(email="user1@example.com").first()
        user2 = User.query.filter_by(email="user2@example.com").first()
        user3 = User.query.filter_by(email="user3@example.com").first()

        if not user1 or not user2 or not user3:
            raise Exception("Users not found. Please seed users first.")

        # Create DSMetrics instance
        ds_metrics = DSMetrics(number_of_models="5", number_of_features="50")
        seeded_ds_metrics = self.seed([ds_metrics])[0]

        # Create DSMetaData instances
        ds_meta_data_list = [
            DSMetaData(
                deposition_id=1 + i,
                title=f"Sample dataset {i+1}",
                description=f"Description for dataset {i+1}",
                publication_type=PublicationType.DATA_MANAGEMENT_PLAN,
                publication_doi=f"10.1234/dataset{i+1}",
                dataset_doi= f"10.1234/dataset{i+1}" if i % 2 == 1  else None,
                tags="tag1, tag2",
                ds_metrics_id=seeded_ds_metrics.id,
            )
            for i in range(5)
        ]
        ds_meta_data_list.append(
            DSMetaData(
                deposition_id=6,
                title="Sample dataset 6",
                description="Description for dataset 6 staged",
                publication_type=PublicationType.DATA_MANAGEMENT_PLAN,
                publication_doi="10.1234/dataset6",
                dataset_doi="10.1234/dataset6",
                tags="tag2",
                dataset_status=DatasetStatus.STAGED,
                ds_metrics_id=seeded_ds_metrics.id,
            )
        )
        ds_meta_data_list.append(
            DSMetaData(
                deposition_id=7,
                title="Sample dataset 7",
                description="Description for dataset 7 published",
                publication_type=PublicationType.DATA_MANAGEMENT_PLAN,
                publication_doi="10.1234/dataset7",
                dataset_doi="10.1234/dataset7",
                tags="tag1",
                dataset_status=DatasetStatus.PUBLISHED,
                ds_metrics_id=seeded_ds_metrics.id,
            )
        )
        seeded_ds_meta_data = self.seed(ds_meta_data_list)

        # Create Author instances and associate with DSMetaData
        authors = [
            Author(
                name=f"Author {i+1}",
                affiliation=f"Affiliation {i+1}",
                orcid=f"0000-0000-0000-000{i}",
                ds_meta_data_id=seeded_ds_meta_data[i % 4].id,
            )
            for i in range(5)
        ]

        self.seed(authors)

        # Create DataSet instances
        datasets = [
            DataSet(
                user_id=user1.id if i % 2 == 0 else user2.id,
                ds_meta_data_id=seeded_ds_meta_data[i].id,
                created_at=datetime.now(timezone.utc),
            )
            for i in range(4)
        ]
        datasets.append(
            DataSet(
                user_id=user1.id,
                ds_meta_data_id=seeded_ds_meta_data[
                    4
                ].id,  # Corresponde a dataset 5 (STAGED)
                created_at=datetime.now(timezone.utc),
            )
        )

        datasets.append(
            DataSet(
                user_id=user2.id,
                ds_meta_data_id=seeded_ds_meta_data[
                    5
                ].id,  # Corresponde a dataset 6 (PUBLISHED)
                created_at=datetime.now(timezone.utc),
            )
        )
        datasets.append(
            DataSet(
                user_id=user3.id,
                ds_meta_data_id=seeded_ds_meta_data[4].id,
                created_at=datetime.now(timezone.utc),
            )
        )
        seeded_datasets = self.seed(datasets)

        # Create DatasetRating for the datasets
        ratings = [
            DatasetRating(dataset_id=seeded_datasets[0].id, user_id=user1.id, rating=4),
            DatasetRating(dataset_id=seeded_datasets[0].id, user_id=user2.id, rating=5),
            DatasetRating(dataset_id=seeded_datasets[1].id, user_id=user1.id, rating=3),
            DatasetRating(dataset_id=seeded_datasets[1].id, user_id=user3.id, rating=4),
            DatasetRating(dataset_id=seeded_datasets[2].id, user_id=user2.id, rating=2),
            DatasetRating(dataset_id=seeded_datasets[2].id, user_id=user3.id, rating=5),
            DatasetRating(dataset_id=seeded_datasets[3].id, user_id=user1.id, rating=4),
            DatasetRating(dataset_id=seeded_datasets[3].id, user_id=user3.id, rating=3),
        ]
        self.seed(ratings)

        # Assume there are 12 UVL files, create corresponding FMMetaData and FeatureModel
        fm_meta_data_list = [
            FMMetaData(
                uvl_filename=f"file{i+1}.uvl",
                title=f"Feature Model {i+1}",
                description=f"Description for feature model {i+1}",
                publication_type=PublicationType.SOFTWARE_DOCUMENTATION,
                publication_doi=f"10.1234/fm{i+1}",
                tags="tag1, tag2",
                uvl_version="1.0",
            )
            for i in range(12)
        ]
        seeded_fm_meta_data = self.seed(fm_meta_data_list)

        # Create Author instances and associate with FMMetaData
        fm_authors = [
            Author(
                name=f"Author {i+5}",
                affiliation=f"Affiliation {i+5}",
                orcid=f"0000-0000-0000-000{i+5}",
                fm_meta_data_id=seeded_fm_meta_data[i].id,
            )
            for i in range(12)
        ]
        self.seed(fm_authors)

        feature_models = [
            FeatureModel(
                data_set_id=seeded_datasets[i // 3].id,
                fm_meta_data_id=seeded_fm_meta_data[i].id,
            )
            for i in range(12)
        ]
        seeded_feature_models = self.seed(feature_models)

        # Create files, associate them with FeatureModels and copy files
        load_dotenv()
        working_dir = os.getenv("WORKING_DIR", "")
        src_folder = os.path.join(
            working_dir, "app", "modules", "dataset", "uvl_examples"
        )
        for i in range(12):
            file_name = f"file{i+1}.uvl"
            feature_model = seeded_feature_models[i]
            dataset = next(
                ds for ds in seeded_datasets if ds.id == feature_model.data_set_id
            )
            user_id = dataset.user_id

            dest_folder = os.path.join(
                working_dir, "uploads", f"user_{user_id}", f"dataset_{dataset.id}"
            )
            os.makedirs(dest_folder, exist_ok=True)
            shutil.copy(os.path.join(src_folder, file_name), dest_folder)

            file_path = os.path.join(dest_folder, file_name)

            uvl_file = Hubfile(
                name=file_name,
                checksum=f"checksum{i+1}",
                size=os.path.getsize(file_path),
                feature_model_id=feature_model.id,
            )
            self.seed([uvl_file])
