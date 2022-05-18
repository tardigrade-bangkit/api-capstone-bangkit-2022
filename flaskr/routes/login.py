import json
from requests import Response
from flaskr.model import db, Users
from flaskr.__init__ import app
from flask import jsonify, request
from flask_bcrypt import check_password_hash



