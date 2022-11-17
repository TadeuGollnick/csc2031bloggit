from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError


def character_check(form, field):
    excluded_chars = "*<", "*%", "*&"

    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(f"Character {char} is not allowed.")


class RegisterForm(FlaskForm):
    username = EmailField(validators=[DataRequired(), character_check])
    password = PasswordField(validators=[DataRequired(), Length(min=8, max=15), character_check])
    confirm = PasswordField()
    submit = SubmitField()
