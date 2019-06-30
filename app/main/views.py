from flask import render_template,request,redirect,url_for,flash,abort
from . import main
from ..comments import Comments
from ..user import User,Pitch
from .forms import CommentsForm,PitchForm,UpdateProfile
from flask_login import login_required
from .. import db


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
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
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

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)