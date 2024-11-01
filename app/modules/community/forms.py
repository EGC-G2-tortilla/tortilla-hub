from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CommunityForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired(), Length(max=256)])
    description = TextAreaField('Description', validators=[DataRequired()])
    url = TextAreaField('URL', validators=[DataRequired()])

    # TODO: add tags
    # TODO: add users

    submit = SubmitField('Save community')
