from flask import render_template
from app.modules.community_join_request import community_join_request_bp


@community_join_request_bp.route('/community_join_request', methods=['GET'])
def index():
    return render_template('community_join_request/index.html')
