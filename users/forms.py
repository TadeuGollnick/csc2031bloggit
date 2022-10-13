from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    username = EmailField(validators=[DataRequired])
    password = PasswordField(validators=[DataRequired])
    confirm = PasswordField()
    submit = SubmitField()
