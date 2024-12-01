from app.modules.community_join_request.models import CommunityJoinRequest
from core.repositories.BaseRepository import BaseRepository


class CommunityJoinRequestRepository(BaseRepository):
    def __init__(self):
        super().__init__(CommunityJoinRequest)

    def get_request_by_id(self, request_id: int) -> CommunityJoinRequest:
        return self.model.query.filter_by(id=request_id).first()

    def get_request_by_user_id_and_community_id(self,
                                                user_who_wants_to_join_id: int,
                                                community_id: int) -> CommunityJoinRequest:
        return self.model.query.filter_by(
            user_who_wants_to_join_id=user_who_wants_to_join_id, community_id=community_id).first()

    def get_all_request_by_community_id(self, community_id: int) -> CommunityJoinRequest:
        return self.model.query.filter_by(community_id=community_id).all()
