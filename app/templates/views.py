from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route("/user")
def index():
    """
    view root function that returns the index page and its data
    """
    title = 'Home - pitch your idea'
    return title



@app.route('/')
@app.route("/comments")
def comments():
    """
    view root function that returns the index page and its data
    """
    title = 'users upload your comments'
    return title




if __name__ == '__main__':
    app.run(debug = True)