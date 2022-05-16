from email.mime import application
from hashlib import sha256
import json
from flaskr.model import db, User
from flaskr.__init__ import app
from flask import jsonify, request
from werkzeug.security import generate_password_hash    

@app.route('/user', methods=["POST"])
def add_user():
    data = request.get_json()
    hash_password = generate_password_hash(data['password'], method="sha256")
    new_user = User(name=data['name'], email=data['email'], password=hash_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"msg" : "User created successfully"})
    
@app.route('/user', methods=["GET"])
def get_all_user():
    query = User.query.all()
    all_user = []
    
    for user in query:
        user_data = {}
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['email'] = user.email
        user_data['password'] = user.password
        all_user.append(user_data)
    
    return jsonify({"users" : all_user})

@app.route('/user/<int:id>', methods=["GET"])
def get_one_user(id):
    user = User.query.filter_by(id=id).first()
    
    if not user:
        return jsonify({"msg" : "User not found"})
    
    user_data = {}
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['email'] = user.email
    user_data['password'] = user.password
    
    return jsonify({"user" : user_data})

@app.route('/user/<int:id>', methods=['PUT'])
def update_one_user(id):
    pass
    # user = User.query.filter_by(id=id)
    
    # if not user:
    #     return jsonify({"msg" : "User not found"})
    
    # data = request.get_json()

    # user.name = data["name"]
    # user.email = data["email"]

    # db.session.commit()
    
    # return jsonify({"user" : "User has been updated"})

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_one_user(id):
    user = User.query.filter_by(id=id).first()

    if not user:
        return jsonify({"msg" : "User not found"})
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({"msg" : "User has been deleted"})