from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import ValidationError, DataRequired, Length, EqualTo
from flaskr.model import User

class FormRegister(FlaskForm):
    def validate_username(self, username_to_check):
        username_selected = User.query.filter_by(username=username_to_check).first()
        if username_selected:
            raise ValidationError('Username already taken, get another username!')

    def validate_username(self, email_to_check):
        email_selected = User.query.filter_by(username=email_to_check).first()
        if email_selected:
            raise ValidationError('Email already taken, get another email!')
    
    