from . import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    image = db.Column(db.String(20), nullable=False, default = "default.jpg")
    password = db.Column(db.String(70), nullable=False)
    posts = db.relationship('Post', backref='author', lazy= True)

    def __repr__(self):
        return f'User {self.username}', '{self.image}'
    
    
class Pitch(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(110), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'User {self.title}'
     