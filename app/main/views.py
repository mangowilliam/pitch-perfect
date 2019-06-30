from flask import render_template,request,redirect,url_for
from . import main
from ..comments import Comments
from ..user import User
from .forms import CommentsForm


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home -make the best decition and pitch'
    return render_template('users.html', title = title)

@main.route('/user/comments/new/<int:id>', methods = ['GET','POST'])
def new_comment(id):
    form = CommentsForm()
    

    return render_template('new_review.html', comments_form=form, )