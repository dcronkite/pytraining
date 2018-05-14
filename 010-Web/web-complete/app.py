"""
Main file. Run this with `python app.py`
"""
from reviewer import app, db


# setup configuration options
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///test.db'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = b'\r\x82\xa4>\x05\xf6pl_\x7f'  # os.urandom(12)


# import these and keep them down here
import reviewer.views
from reviewer import models


# setup database
def setup_db():
    db.create_all()
    u = models.User(username='David')
    db.session.add(u)
    r = models.Record(text='It is only May.')
    db.session.add(r)
    db.session.commit()


setup_db()  # add user/records
app.run()  # run application
