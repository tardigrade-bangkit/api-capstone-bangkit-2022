from flaskr.__init__ import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flaskr.__init__ import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), unique=False, nullable=False)
    email = db.Column(db.String(length=50), unique=True, nullable=False)
    password = db.Column(db.String(length=20), nullable=False)
    
    @property
    def encode_password(self):
        return self.encode_password
    
    @encode_password.setter
    def encode_password(self, password_to_hash):
        self.password = bcrypt.generate_password_hash(password_to_hash).decode("utf-8")
        
    # def check_password(self, password_to_check):
        