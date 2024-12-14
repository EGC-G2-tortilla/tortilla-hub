from app.modules.featuremodel.models import UVLParser
from app.modules.flamapy.repositories import FlamapyRepository
from core.services.BaseService import BaseService


class FlamapyService(BaseService):
    def __init__(self):
        self.repository = FlamapyRepository()

    def calculate_fact_labels_from_uvl(self, uvl_file_path):
        """
        Calcula los fact labels a partir de un archivo UVL.
        """
        try:
            parser = UVLParser()
            model_data = parser.parse(uvl_file_path)
            return {
                "number_of_features": len(model_data.get("features", [])),
                "constraints_count": len(model_data.get("constraints", [])),
                "max_depth": model_data.get("max_depth", 0),
                "variability": model_data.get("variability", 0.0),
            }
        except Exception as e:
            raise RuntimeError(f"Error processing UVL file: {str(e)}")
