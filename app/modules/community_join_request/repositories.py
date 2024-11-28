from app.modules.community_join_request.models import CommunityJoinRequest
from core.repositories.BaseRepository import BaseRepository


class CommunityJoinRequestRepository(BaseRepository):
    def __init__(self):
        super().__init__(CommunityJoinRequest)
