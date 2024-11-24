from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, URL


class CommunityForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=256)])
    description_info = TextAreaField(
        "Description", validators=[DataRequired(), Length(max=30000)]
    )
    url = URLField("URL", validators=[DataRequired(), URL()])

    submit = SubmitField("Save community")
