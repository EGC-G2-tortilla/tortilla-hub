from core.blueprints.base_blueprint import BaseBlueprint

community_join_request_bp = BaseBlueprint(
    "community_join_request", __name__, template_folder="templates"
)
