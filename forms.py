from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, URLField, TextAreaField
from wtforms.validators import InputRequired, URL, Optional, NumberRange

class PetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet's name cannot be blank")])
    species = SelectField("Species", choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')], validators=[InputRequired(message="Pet's species must be selected")])
    photo_url = URLField("Photo URL", validators=[Optional(), URL(message='You must use a valid URL')])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes', validators=[Optional()])
    available= BooleanField("Available?")