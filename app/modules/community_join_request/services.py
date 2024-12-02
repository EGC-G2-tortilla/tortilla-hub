from app.modules.community_join_request.repositories import (
    CommunityJoinRequestRepository,
)
from app.modules.community.services import CommunityService
from app.modules.community_join_request.models import CommunityJoinRequest
from core.services.BaseService import BaseService

community_service = CommunityService()


class CommunityJoinRequestService(BaseService):
    def __init__(self):
        super().__init__(CommunityJoinRequestRepository())

    def create_from_request(self, current_user, community) -> CommunityJoinRequest:
        # Si el usuario ya esta en la comunidad, no tiene sentido que se cree la request
        if community_service.is_user_in_community(current_user, community):
            return False

        request = self.create(
            user_who_wants_to_join_id=current_user.id, community_id=community.id
        )
        return request

    def get_request_by_id(self, request_id: int) -> CommunityJoinRequest:
        return self.repository.get_request_by_id(request_id)

    def has_user_sent_a_request(self, user_who_wants_to_join, community) -> bool:
        # check if user and community has id

        try:
            if community_service.is_user_in_community(user_who_wants_to_join, community):
                return False

            user_who_wants_to_join_id = user_who_wants_to_join.id
            community_id = community.id
            if (not user_who_wants_to_join_id) and (not community_id):
                return False
        except Exception:
            return False

        request = self.repository.get_request_by_user_id_and_community_id(
            user_who_wants_to_join_id, community_id
        )

        print(request)

        if request:
            return True
        else:
            return False

    def get_all_request_by_community_id(
        self, community_id: int
    ) -> CommunityJoinRequest:
        return self.repository.get_all_request_by_community_id(community_id)

    def accept_request(self, current_user, community, request: CommunityJoinRequest):
        if request.user_who_wants_to_join_id != current_user.id or request.community_id != community.id:
            print("FAILING")
            return False

        community_service.join_a_community(current_user, community)
        request.delete()

    def decline_request(self, request):
        request.delete()
