from app.modules.community_join_request.models import CommunityJoinRequest
from core.repositories.BaseRepository import BaseRepository


class CommunityJoinRequestRepository(BaseRepository):
    def __init__(self):
        super().__init__(CommunityJoinRequest)

    def get_request_by_id(self, request_id: int) -> CommunityJoinRequest:
        return self.model.query.filter_by(request_id=request_id)
