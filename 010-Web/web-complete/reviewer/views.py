from reviewer import app, models


@app.route('/hello')
def hello():
    return '<h1>Hello world</h1>'


@app.route('/review')
def review():
    records = models.Record.query.all()
    return records[0].text
