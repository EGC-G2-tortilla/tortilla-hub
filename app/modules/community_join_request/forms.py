from flask_wtf import FlaskForm
from wtforms import SubmitField


class CommunityJoinRequestForm(FlaskForm):
    submit = SubmitField('Save community_join_request')
