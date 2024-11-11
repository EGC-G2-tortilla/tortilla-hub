from app.modules.community.repositories import CommunityRepository
from core.services.BaseService import BaseService


class CommunityService(BaseService):
    def __init__(self):
        super().__init__(CommunityRepository())

    def get_all_communities(self):
        return self.repository.get_all_communities()

    def get_community_by_name(self, community_name: str):
        return self.repository.get_community_by_name(community_name)
    
    def is_user_in_community(self,current_user, community):
        res = current_user in community.members
        return res

    def join_a_community(self, current_user, community):
        community.members.append(current_user)

        self.update(community.id, members=community.members)
