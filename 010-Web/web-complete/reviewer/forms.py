from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, RadioField, StringField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class ReviewForm(FlaskForm):
    comments = TextAreaField('Comments')
    options = RadioField (
        'Answers',
        choices=[
            ('1', 'Yes'),
            ('2', 'No')],
     )
    submit = SubmitField('Submit Record')
