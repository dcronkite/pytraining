from reviewer import db


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    answer = db.Column(db.Integer)
    comments = db.Column(db.String(200))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Record:{self.id}>'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f'<User{self.id}:{self.username}>'
