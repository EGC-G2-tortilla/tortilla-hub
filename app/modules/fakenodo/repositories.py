from app.modules.fakenodo.models import Fakenodo
from core.repositories.BaseRepository import BaseRepository


class FakenodoRepository(BaseRepository):
    def __init__(self):
        super().__init__(Fakenodo)
    
    def get_by_dataset_id(self, dataset_id: int):
        dataset = self.model.query.filter_by(dataset_id=dataset_id).first()
        return dataset if dataset else None 
