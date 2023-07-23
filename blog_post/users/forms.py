from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Email, EqualTo, DataRequired
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from blog_post.models import User


class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Log In')


def validate_username(username):
    user = User.query.filter_by(username=username.data).first()
    if user and user != current_user:
        raise ValidationError('Your username has been registered already!')


def validate_email(email):
    user = User.query.filter_by(email=email.data).first()
    if user and user != current_user:
        raise ValidationError('Your email has been registered already!')


class RegistrationForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email()])
    username = StringField('UserName:', validators=[DataRequired()])
    password = PasswordField('Password:',
                             validators=[DataRequired(), EqualTo('pass_confirm', message='Password must match!')])
    pass_confirm = PasswordField('Confirm Password:', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):
        validate_email(email)

    def validate_username(self, username):
        validate_username(username)


class UpdateUserForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email()])
    username = StringField('Username:', validators=[DataRequired()])
    picture = FileField('Update Profile Picture:', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_email(self, email):
        validate_email(email)

    def validate_username(self, username):
        validate_username(username)
