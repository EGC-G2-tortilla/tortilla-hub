from app.modules.community_join_request.repositories import CommunityJoinRequestRepository
from app.modules.community.services import CommunityService
from app.modules.community_join_request.models import CommunityJoinRequest
from core.services.BaseService import BaseService


class CommunityJoinRequestService(BaseService):
    def __init__(self):
        super().__init__(CommunityJoinRequestRepository())

    def create_from_request(self, current_user, community) -> CommunityJoinRequest:
        self.create(user_who_wants_to_join_id=current_user.id,
                    community_id=community.id)

    def get_request_by_id(self, request_id: int) -> CommunityJoinRequest:
        return self.get_request_by_id(request_id)

    def get_all_request_by_community_id(self, community_id: int) -> CommunityJoinRequest:
        return self.get_all_request_by_community_id(community_id)

    def accept_request(self, current_user, community, request):
        CommunityService.join_a_community(current_user, community)
        self.delete(request)

    def decline_request(self, request):
        self.delete(request)
