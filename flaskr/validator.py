from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import ValidationError, DataRequired, Length, EqualTo, Email
from flaskr.model import User

class FormRegister(FlaskForm):
    def validate_email(self, email_to_check):
        email_selected = User.query.filter_by(email=email_to_check).first()
        if email_selected:
            raise ValidationError('Email already taken, get another email!')
        
    name = StringField(label="name", validators=[Length(min=2), DataRequired()])
    email = StringField(label="email", validators=[Email(), DataRequired()])
    password = PasswordField(label="password", validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(label="confirm password", validators=[EqualTo('password'), DataRequired()])
        
class FormLogin(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    
    