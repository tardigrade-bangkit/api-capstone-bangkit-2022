from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt

# csrf = CSRFProtect()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/bangkit.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkeyawesome'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
# csrf.init_app(app)

from flaskr.route import users



