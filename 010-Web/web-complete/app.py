from reviewer import app, db


app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///test.db'
app.config['DEBUG'] = True

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


setup_db()
app.run()
