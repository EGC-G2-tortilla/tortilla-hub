import logging

from flask import render_template

from app.modules.community.services import CommunityService
from app.modules.community import community_bp

logger = logging.getLogger(__name__)


@community_bp.route('/community', methods=['GET'])
def index():
    logger.info("Access community index")
    community_service = CommunityService()


    # Statistics: total size of all datasets
    # TODO: intentar que se haga solo con los datasets sincronizados por que no sabemos como son los otros
    communities = community_service.get_all_communities()
    #total_size = sum(dataset.get_file_total_size() for dataset in total_datasets)
    #total_size = SizeService().get_human_readable_size(total_size)

    return render_template(
        "community/index.html",

        communities=communities
    )
    

