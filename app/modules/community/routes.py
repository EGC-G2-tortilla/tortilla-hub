import logging

from flask import (
    render_template,
    abort,
    request
)
from flask_login import login_required, current_user

from app.modules.community.services import CommunityService
from app.modules.community.forms import CommunityForm
from app.modules.dataset.services import DataSetService
from app.modules.community import community_bp

logger = logging.getLogger(__name__)

community_service = CommunityService()
dataset_service = DataSetService()


@community_bp.route('/community', methods=['GET'])
def index():
    logger.info("Access community index")

    communities = community_service.get_all_communities()

    return render_template(
        "community/index.html",

        communities=communities
    )


@community_bp.route("/community/<string:community_name>/", methods=["GET"])
def get_community_by_name(community_name):
    community = community_service.get_community_by_name(community_name)

    if not community:
        abort(404)

    is_user_in_community = community_service.is_user_in_community(current_user, community)

    datasets = dataset_service.get_by_community_id(community.id)

    return render_template("community/community.html",
                           community=community,
                           user_in_community=is_user_in_community,
                           datasets=datasets)


@community_bp.route("/community/<string:community_name>/info", methods=["GET"])
def get_community_info_by_name(community_name):
    community = community_service.get_community_by_name(community_name)

    if not community:
        abort(404)

    is_user_in_community = community_service.is_user_in_community(current_user, community)

    return render_template("community/community_info.html",
                           user_in_community=is_user_in_community,
                           community=community)


@community_bp.route("/community/<string:community_name>/members", methods=["GET"])
def get_community_members_by_name(community_name):
    community = community_service.get_community_by_name(community_name)

    if not community:
        abort(404)

    is_user_in_community = community_service.is_user_in_community(current_user, community)

    return render_template("community/community_members.html",
                           user_in_community=is_user_in_community,
                           community=community)


@community_bp.route("/community/create", methods=["GET", "POST"])
@login_required
def create_community():
    form = CommunityForm()
    if request.method == "POST":
        if not form.validate_on_submit():
            return [{"message": form.errors}], 400

        try:
            logger.info("Creating community...")
            community = community_service.create_from_form(form=form, current_user=current_user)
            logger.info(f"Created community: {community}")
        except Exception as exc:
            logger.exception(f"Exception while create community data in local {exc}")
            return [{"Exception while create community data in local: ": str(exc)}], 400

        msg = "Everything works!"
        return [{"message": msg}], 200

    return render_template("community/create_community.html", form=form)


@community_bp.route("/community/<string:community_name>/join", methods=["POST"])
@login_required
def join_a_community(community_name):
    community = community_service.get_community_by_name(community_name)

    if not community:
        abort(404)

    community_service.join_a_community(current_user, community)
    is_user_in_community = community_service.is_user_in_community(current_user, community)

    return render_template("community/community_members.html",
                           user_in_community=is_user_in_community,
                           community=community)
