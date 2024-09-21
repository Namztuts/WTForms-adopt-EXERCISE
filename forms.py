from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional, URL, Length

species_choices = ['Cat','Dog','Porcupine']
age_choices = [num for num in range(31)]


class PetForm (FlaskForm):
    '''Form to add a pet for adoption'''
    
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices = [(choice, choice) for choice in species_choices])
    age = SelectField('Age', choices= [(choice, choice) for choice in age_choices])
    notes = TextAreaField('Notes', validators=[Optional(), Length(min=10)])
    photo_url = StringField('Photo URL', validators=[Optional(),URL()])


class EditPetForm(FlaskForm):
    '''Form for editing an existing pet'''

    notes = TextAreaField('Notes', validators=[Optional(), Length(min=10)])
    photo_url = StringField('Photo URL', validators=[Optional(),URL()])
    available = BooleanField("Available?") #automatically converts to a checkbox in the form