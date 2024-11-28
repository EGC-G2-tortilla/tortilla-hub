from app.modules.community_join_request.repositories import CommunityJoinRequestRepository
from core.services.BaseService import BaseService


class CommunityJoinRequestService(BaseService):
    def __init__(self):
        super().__init__(CommunityJoinRequestRepository())
