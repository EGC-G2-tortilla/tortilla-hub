from app.modules.featuremodel.repositories import (
    FMMetaDataRepository,
    FeatureModelRepository,
)
from app.modules.hubfile.services import HubfileService
from core.services.BaseService import BaseService


class FeatureModelService(BaseService):
    def __init__(self):
        super().__init__(FeatureModelRepository())
        self.hubfile_service = HubfileService()

    def total_feature_model_views(self) -> int:
        return self.hubfile_service.total_hubfile_views()

    def total_feature_model_downloads(self) -> int:
        return self.hubfile_service.total_hubfile_downloads()

    def count_feature_models(self):
        return self.repository.count_feature_models()

    def get_fact_labels(self, feature_model_id):
        """
        Devuelve los fact labels para un modelo de características dado.
        """
        feature_model = self.get_by_id(feature_model_id)
        return feature_model.get_fact_labels()

    class FMMetaDataService(BaseService):
        def __init__(self):
            super().__init__(FMMetaDataRepository())
