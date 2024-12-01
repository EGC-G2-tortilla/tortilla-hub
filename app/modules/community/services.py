from app.modules.community.repositories import CommunityRepository
from core.services.BaseService import BaseService


class CommunityService(BaseService):
    def __init__(self):
        super().__init__(CommunityRepository())

    def get_all_communities(self):
        return self.repository.get_all_communities()

    def get_community_by_id(self, community_id: id):
        return self.repository.get_community_by_id(community_id)

    def get_community_by_name(self, community_name: str):
        return self.repository.get_community_by_name(community_name)

    def is_user_in_community(self, current_user, community):
        res = current_user in community.members
        return res

    def join_a_community(self, current_user, community):
        community.members.append(current_user)

        self.update(community.id, members=community.members)

    def create_from_form(self, current_user, form):
        community = self.create(
            name=form.data["name"],
            description=form.data["description_info"],
            url=form.data["url"],
            admin=current_user.id,
            members=[current_user],
        )
        return community
