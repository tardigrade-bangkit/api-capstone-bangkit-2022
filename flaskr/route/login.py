from requests import Response
from flaskr.model import db, User
from flaskr.__init__ import app
from flask import jsonify, request
from werkzeug.security import generate_password_hash

# @app.route('/login', methods=["POST"])
# def user_login():
    
