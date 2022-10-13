from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, EqualTo, Length


class RegisterForm(FlaskForm):
    username = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired(), Length(min=8, max=15)])
    confirm = PasswordField()
    submit = SubmitField()
