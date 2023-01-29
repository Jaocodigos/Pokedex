from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DexForm(FlaskForm):
    style = {'class_field': {'class': 'poke-input'},
             'class_button': {'class': 'dex-btn animate'}}
    name = StringField('name', validators=[DataRequired()], render_kw=style['class_field'])
    button = SubmitField('Search', render_kw=style['class_button'])
