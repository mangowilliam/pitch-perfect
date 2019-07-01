from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentsForm(FlaskForm):

    comment = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title= StringField('Title',validators=[Required()])
    pitch = TextAreaField('pitch', validators=[Required()])
    submit = SubmitField('pitches') 
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('content.',validators = [Required()])
    submit = SubmitField('Submit')