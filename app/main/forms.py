from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required

class CommentsForm(FlaskForm):

    comment = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title= StringField('Title',validators=[Required()])
    content = TextAreaField('pitch', validators=[Required()])
    category = RadioField('Label', choices=[ ('startupspitch','startupspitch'), ('charitypitch','charitypitch'),('eventspitch','eventspitch')],validators=[Required()])
	
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	content = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField()
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('content.',validators = [Required()])
    submit = SubmitField('Submit')