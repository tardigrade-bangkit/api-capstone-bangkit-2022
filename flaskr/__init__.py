from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import os

# database_path = os.path.abspath(os.getcwd())+"\database\bangkit.db"
# csrf = CSRFProtect()

app = Flask(__name__)
api = Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/'+database_path
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'oiwerjowjeorwjeorjweorjweorj'
# db = SQLAlchemy(app)
# csrf.init_app(app)

from flaskr import route



