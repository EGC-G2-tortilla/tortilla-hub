import logging

from flask import (
    render_template,
    abort
)

from app.modules.community.services import CommunityService
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

    datasets = dataset_service.get_by_community_id(community.id)

    return render_template("community/community.html",
                           community=community,
                           datasets=datasets)


@community_bp.route("/community/<string:community_name>/info", methods=["GET"])
def get_community_info_by_name(community_name):
    community = community_service.get_community_by_name(community_name)

    if not community:
        abort(404)

    return render_template("community/community_info.html",
                           community=community)
