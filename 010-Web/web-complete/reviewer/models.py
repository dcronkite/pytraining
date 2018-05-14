"""
Sqlalchemy orm models
These will be used to automatically create and more easily handle the backend
"""
from reviewer import db


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    answer = db.Column(db.Integer)
    comments = db.Column(db.String(200))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        """So we can actually see what we're working with"""
        return f'<Record:{self.id}>'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        """So we can see what we're working with"""
        return f'<User{self.id}:{self.username}>'
