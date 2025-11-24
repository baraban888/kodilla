from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from blog.config import Config

class EntryForm(FlaskForm):
    title = StringField(
        'Tytuł wpisu',
        validators=[DataRequired()]
    )
    body = TextAreaField(
        'Treść',
        validators=[DataRequired()]
    )
    is_published = BooleanField('Wpis opublikowany')

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    def validate_username(self, field):
        if field.data != Config.ADMIN_USERNAME:
            raise ValidationError("Invalid username")

    def validate_password(self, field):
        if field.data != Config.ADMIN_PASSWORD:
            raise ValidationError("Invalid password")
