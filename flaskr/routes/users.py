from datetime import datetime, timedelta
from functools import wraps
import json
from types import MethodDescriptorType
import uuid ,jwt
from multiprocessing import AuthenticationError
from flaskr.model import Lessons, Lessons_Content, Users, Children, db
from flaskr.__init__ import app, secret
from flask import jsonify, request
from flask_bcrypt import check_password_hash


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            data = jwt.decode(token, secret)
            current_user = Users.query.filter_by(public_id = data['public_id']).first()
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        return  f(current_user, *args, **kwargs)
  
    return decorated

@app.route('/users', methods=["POST"])
def add_user():
    
    data = request.get_json()
    selected_email = Users.query.filter_by(email=data["email"]).first()
    if selected_email:
        return jsonify({"msg" : "User already taken, try with another email!"}), 400
    
    new_user = Users(public_id=str(uuid.uuid4()), name=data['name'], email=data['email'], encode_password=data['password'], pin=0)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"msg" : "Created user successfully"}), 201
    
@app.route('/users', methods=["GET"])
@token_required
def get_all_user():
    query = Users.query.all()
    all_user = []
    
    for user in query:
        user_data = {}
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['email'] = user.email
        user_data['password'] = user.password
        
        all_user.append(user_data)
    
    return jsonify({"users" : all_user})

@app.route('/users/<int:id>', methods=["GET"])
def get_one_Users(id):
    user = Users.query.filter_by(id=id).first()
    
    if not user:
        return jsonify({"msg" : "User not found"}), 401
    
    user_data = {}
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['email'] = user.email
    user_data['password'] = user.password
    
    return jsonify({"user" : user_data})

@app.route('/users/<int:id>', methods=['PUT'])
def update_one_user(id):
    user = Users.query.filter_by(id=id).first()
    if not user:
        return jsonify({"msg" : "User not found"}), 401
    
    data = request.get_json()

    user.name = data["name"]
    user.email = data["email"]

    db.session.commit()
    
    return jsonify({"user" : "User has been updated"}), 201

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_one_user(id):
    user = Users.query.filter_by(id=id).first()

    if not user:
        return jsonify({"msg" : "User not found"}), 401
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({"msg" : "User has been deleted"}), 201


@app.route('/login', methods=["POST"])
def user_login():
    data = request.get_json()
    selected_user = Users.query.filter_by(email=data["email"]).first()

    if not selected_user:
        return jsonify({"msg" : "Invalid authorization "}), 404

    if check_password_hash(selected_user.password, data["password"]):
        token = jwt.encode({
            'public_id': selected_user.public_id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, secret, algorithm="HS256")
        return jsonify({'token' : token}), 201

    return jsonify({"msg" : "Invalid password"}), 404

@app.route('/users/pin', methods=["POST"])
def add_pin():
    data = request.get_json()
    selected_user = Users.query.filter_by(email=data["email"]).first()
    
    if selected_user.pin != 0:
        return jsonify({"msg" : "User already have pin"})
    
    selected_user.pin = data["pin"]
    db.session.commit()
    
    return jsonify({'msg' : 'Pin added successfully'})

@app.route('/users/pin/check', methods=['POST'])
def check_pin():
    data = request.get_json()
    selected_user = Users.query.filter_by(email=data["email"]).first()
    
    if selected_user != 0:
        return jsonify({"msg" : "user already have pin"})
    
    return jsonify({"msg" : "user don't have pin"})



@app.route('/users/<int:id>/children', methods=["POST"])
def add_children(id):
    data = request.get_json()
    new_children = Children(name=data['name'], level=0, Users_id=id)
    
    db.session.add(new_children)
    db.session.commit()
    
    return jsonify({"msg" : "Created children successfully"}), 201

@app.route('/users/<int:id>/children', methods=['GET'])
def get_all_children(id):

    query = Children.query.filter_by(Users_id=id)
    all_children = []
    
    for children in query:
        children_data = {}
        children_data['id'] = children.id
        children_data['name'] = children.name
        children_data['level'] = children.level
        
        all_children.append(children_data)
    
    return jsonify({"users" : all_children})

@app.route('/users/<int:id>/children/<int:children_id>', methods=['GET'])
def get_one_children(children_id, id):
    children = Children.query.filter_by(id=children_id, Users_id=id).first()
    if not children:
        return jsonify({"msg" : "Children not found"}), 401
    
    children_data = {}
    children_data['id'] = children.id
    children_data['name'] = children.name
    children_data['level'] = children.level
    
    return jsonify({"user" : children_data})


@app.route('/users/<int:id>/children/<int:children_id>', methods=['PUT'])
def update_one_children(children_id, id):
    selected_children = Children.query.filter_by(id=children_id, Users_id=id).first()
    if not selected_children:
        return jsonify({"msg" : "Children not found"}), 401
    
    data = request.get_json()

    selected_children.name = data["name"]

    db.session.commit()
    
    return jsonify({"user" : "Children has been updated"}), 201


@app.route('/users/<int:id>/children/<int:children_id>', methods=['DELETE'])
def delete_one_children(children_id, id):
    children = Children.query.filter_by(id=children_id, Users_id=id).first()

    if not children:
        return jsonify({"msg" : "Children not found"}), 401
    
    db.session.delete(children)
    db.session.commit()
    
    return jsonify({"msg" : "Children has been deleted"}), 201


@app.route('/lessons', methods=['GET'])
def get_lesson():
    data = request.get_json()
    query = Lessons.query.filter_by(level=data['level'])
    
    if not query:
        return jsonify({"msg" : "Lessons not found"})
    
    lessons_with_same_level = []
    
    for lessons in query:
        list_lessons = {}
        list_lessons['id'] = lessons.id
        list_lessons['title'] = lessons.title
        list_lessons['cover_image'] = lessons.cover_image
        list_lessons['type'] = lessons.type
        
        lessons_with_same_level.append(list_lessons)
    
    return jsonify({"users" : lessons_with_same_level})


@app.route('/lessons/<int:id>', methods=['GET'])
def get_lessons_content(id):
    selected_lessons = Lessons_Content.query.filter_by(Lessons_id=id)
    
    if not selected_lessons:
        return jsonify({"msg" : "Lessons not found"}), 401
    
    all_lessons_content = []
    
    for lessons_content in selected_lessons:
        lessons_content_data = {}
        lessons_content_data['id'] = lessons_content.id
        lessons_content_data['title'] = lessons_content.title
        lessons_content_data['type'] = lessons_content.type
        lessons_content_data['order'] = lessons_content.order
        
        all_lessons_content.append(lessons_content_data)
    
    return jsonify({"Lessons content" : all_lessons_content})


