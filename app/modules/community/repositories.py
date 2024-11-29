from app.modules.community.models import Community
from core.repositories.BaseRepository import BaseRepository


class CommunityRepository(BaseRepository):
    def __init__(self):
        super().__init__(Community)

    def get_all_communities(self):
        return self.model.query.all()

    def get_community_by_name(self, community_name: str) -> Community:
        return self.model.query.filter_by(name=community_name).first()
    
    def get_community_by_id(self, community_id: int) -> Community:
        return self.model.query.filter_by(id=community_id).first()
