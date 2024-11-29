from flask import abort, redirect
from flask_login import login_required, current_user
from app.modules.community.services import CommunityService
from app.modules.community_join_request.services import CommunityJoinRequestService
from app.modules.auth.services import AuthenticationService
from app.modules.community_join_request import community_join_request_bp

community_service = CommunityService()
community_join_request_service = CommunityJoinRequestService()
user_service = AuthenticationService()


@community_join_request_bp.route("/community/<string:community_name>/join", methods=["POST"])
@login_required
def join_community(community_name):
    community = community_service.get_community_by_name(community_name)

    if not community:
        abort(404)

    community_join_request_service.create_from_request(current_user, community)
    return redirect("/community/"+community_name)


@community_join_request_bp.route("/community-join-request/<int:request_id>/accept", methods=["POST"])
@login_required
def accept_request(request_id):
    request_join = community_join_request_service.get_request_by_id(request_id)

    if not request_join:
        abort(404)

    community = community_service.get_community_by_id(request_join.community_id)

    if not community:
        abort(404)

    if community.admin != current_user.id:
        abort(503)

    user = user_service.get_by_id(request_join.user_who_wants_to_join_id)

    if not user:
        abort(404)

    community_join_request_service.accept_request(user, community, request_join)

    return redirect("/community/"+community.name+"/members")


@community_join_request_bp.route("/community-join-request/<int:request_id>/decline", methods=["POST"])
@login_required
def decline_request(request_id):
    request_join = community_join_request_service.get_request_by_id(request_id)

    if not request_join:
        abort(404)

    community = community_service.get_community_by_id(request_join.community_id)

    if not community:
        abort(404)

    if community.admin != current_user.id:
        abort(503)

    community_join_request_service.decline_request(request_join)

    return redirect("/community/"+community.name+"/members")
