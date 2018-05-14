from flask import render_template, request, make_response, url_for, redirect, session

from reviewer import app, db, models, forms


@app.route('/hello')
def hello():
    return '<h1>Hello world</h1>'


@app.route('/')
def index():

    if 'username' in session:
        return 'Logged in as {}: <a href="{}">Review</a>'.format(
            session['username'],
            url_for('review')
        )
    return 'You are not logged in: <a href="{}">Login</a>'.format(
        url_for('login')
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if request.method == 'POST':
        session['username'] = form.username.data
        try:
            session['user_id'] = models.User.query.filter_by(username=session['username']).first().id
        except Exception as e:
            raise e
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/review', methods=['GET', 'POST'])
def review():
    form = forms.ReviewForm()
    if form.validate_on_submit():
        record = models.Record.query.filter_by(
            id=session['record_id']
        ).one()
        record.comments = form.comments.data
        record.answer = int(form.options.data)
        record.user = session['user_id']
        db.session.commit()
        redirect(url_for('review'))
    # get next record
    record = models.Record.query.filter(
        models.Record.answer == None
    ).order_by(
        'id'
    ).first()
    session['record_id'] = record.id
    form.options.data = record.answer
    form.comments.data = record.comments
    return render_template('review.html', record=record, form=form)

