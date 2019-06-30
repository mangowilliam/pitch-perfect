from flask import render_template,request,redirect,url_for,flash
from . import main
from ..comments import Comments
from ..user import User,Pitch
from .forms import CommentsForm,PitchForm
from flask_login import login_required


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home -make the best decition and pitch'
    return render_template('users.html', title = title)

@main.route('/user/comments/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentsForm()
    

    return render_template('new_review.html',form=form, )
# Views
@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def pitches():
    form= PitchForm()
    if form.validate_on_submit():
        flash("pitch created",'success')
        return redirect(url_for('home'))

    title = 'Home -new pitch'
    return render_template('pitches.html', title = title, form=form)