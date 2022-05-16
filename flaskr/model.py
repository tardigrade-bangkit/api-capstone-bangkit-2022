from enum import unique

from sqlalchemy import null
from flaskr.__init__ import db
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=50), unique=True, nullable=False)
    email = db.Column(db.String(length=50), unique=True, nullable=False)
    password = db.Column(db.String(length=20), nullable=False)