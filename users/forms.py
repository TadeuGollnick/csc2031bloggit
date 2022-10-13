from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, validators, Form


class RegisterForm(Form):
    username = EmailField()
    password = PasswordField()
    confirm = PasswordField()
    submit = SubmitField()
