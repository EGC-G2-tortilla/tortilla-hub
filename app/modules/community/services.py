from app.modules.community.repositories import CommunityRepository
from core.services.BaseService import BaseService


class CommunityService(BaseService):
    def __init__(self):
        super().__init__(CommunityRepository())
        
    def get_all_communities(self):
        return self.repository.get_all_communities()
