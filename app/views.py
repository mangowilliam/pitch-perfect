from flask import render_template
from app import app
from comments import Comments
from .forms import CommentsForm


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home -make the best decition and pitch'
    return render_template('users.html', title = title)