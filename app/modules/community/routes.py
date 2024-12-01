import logging

from flask import render_template, abort, request, redirect
from flask_login import login_required, current_user

from app.modules.community.services import CommunityService
from app.modules.community.forms import CommunityForm
from app.modules.dataset.services import DataSetService
from app.modules.community_join_request.services import CommunityJoinRequestService
from app.modules.profile.services import UserProfileService
from app.modules.community import community_bp

logger = logging.getLogger(__name__)

community_service = CommunityService()
dataset_service = DataSetService()
community_join_request_service = CommunityJoinRequestService()
profile_service = UserProfileService()


@community_bp.route("/community", methods=["GET"])
def index():
    logger.info("Access community index")

    communities = community_service.get_all_communities()

    return render_template("community/index.html", communities=communities)


@community_bp.route("/community/<string:community_name>/", methods=["GET"])
def get_community_by_name(community_name):
    community = community_service.get_community_by_name(community_name)

    if not community:
        abort(404)

    is_user_in_community = community_service.is_user_in_community(
        current_user, community
    )

    has_user_send_a_request_to_join = False
    if not is_user_in_community:
        has_user_send_a_request_to_join = community_join_request_service.has_user_sent_a_request(
            current_user, community)

    datasets = dataset_service.get_by_community_id(community.id)

    return render_template(
        "community/community.html",
        community=community,
        user_in_community=is_user_in_community,
        datasets=datasets,
        has_user_send_a_request_to_join=has_user_send_a_request_to_join
    )


@community_bp.route("/community/<string:community_name>/info", methods=["GET"])
def get_community_info_by_name(community_name):
    community = community_service.get_community_by_name(community_name)

    if not community:
        abort(404)

    is_user_in_community = community_service.is_user_in_community(
        current_user, community
    )

    has_user_send_a_request_to_join = False
    if not is_user_in_community:
        has_user_send_a_request_to_join = community_join_request_service.has_user_sent_a_request(
            current_user, community)

    return render_template(
        "community/community_info.html",
        user_in_community=is_user_in_community,
        community=community,
        has_user_send_a_request_to_join=has_user_send_a_request_to_join
    )


@community_bp.route("/community/<string:community_name>/members", methods=["GET"])
@login_required
def get_community_members_by_name(community_name):
    community = community_service.get_community_by_name(community_name)

    if not community:
        abort(404)

    is_user_in_community = community_service.is_user_in_community(
        current_user, community
    )
    
    has_user_send_a_request_to_join = False
    if not is_user_in_community:
        has_user_send_a_request_to_join = community_join_request_service.has_user_sent_a_request(
            current_user, community)

    join_requests = []
    if current_user.id == community.admin:
        resquests_to_join = community_join_request_service.get_all_request_by_community_id(community.id)

        join_requests = [profile_service.get_by_user_id(req.user_who_wants_to_join_id)
                         for req in resquests_to_join]

        for x in range(len(join_requests)):
            join_requests[x].id = resquests_to_join[x].id

    return render_template(
        "community/community_members.html",
        user_in_community=is_user_in_community,
        community=community,
        join_requests=join_requests,
        has_user_send_a_request_to_join=has_user_send_a_request_to_join
    )


@community_bp.route("/community/create", methods=["GET", "POST"])
@login_required
def create_community():
    form = CommunityForm()
    if request.method == "POST":
        if not form.validate_on_submit():
            return [{"message": form.errors}], 400

        try:
            logger.info("Creating community...")
            community = community_service.create_from_form(
                form=form, current_user=current_user
            )
            logger.info(f"Created community: {community}")
        except Exception as exc:
            logger.exception(f"Exception while create community data in local {exc}")
            return [{"Exception while create community data in local: ": str(exc)}], 400

        return redirect("/community")

    return render_template("community/create_community.html", form=form)
