from flask import render_template,request,redirect,url_for,flash,abort
from . import main
from ..comments import Comments
from ..user import User,Pitch,Comment
from .forms import CommentForm,PitchForm,UpdateProfile
from flask_login import login_required,login_user,logout_user,current_user
from .. import db


# Views
@main.route('/', methods = ['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.all()
    title = 'Home -make the best decition and pitch'
    startups = Pitch.query.filter_by(category="startupspitch")
    charity = Pitch.query.filter_by(category = "charitypitch")
    events = Pitch.query.filter_by(category = "eventspitch")
    return render_template('users.html', title = title,pitches=pitches,charity=charity,events=events,startups=startups)

@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        content = form.content.data

        new_comment = Comment(content = content, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('.new_comment', pitch_id= pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comments.html', form = form, comment = all_comments, pitch = pitch )
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
        content = form.content.data
        title = form.title.data
        user_id= current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        pitch =Pitch(user_id = current_user._get_current_object().id, title = title,content=content,category=category)
        db.session.add(pitch)
        db.session.commit()
        flash('pitch created','succesful')
        return redirect(url_for('main.index',))

    title = 'Home -new pitch'
    return render_template('pitches.html',form=form)

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



