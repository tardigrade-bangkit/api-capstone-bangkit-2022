from flaskr.model import db, User
from flaskr.__init__ import app
from flask import jsonify, request
from flask_bcrypt import check_password_hash

@app.route('/users', methods=["POST"])
def add_user():
    data = request.get_json()
    selected_email = User.query.filter_by(email=data["email"]).first()
    if selected_email:
        return jsonify({"msg" : "User already taken, try with another email!"}), 400
    
    new_user = User(name=data['name'], email=data['email'], encode_password=data['password'])
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"msg" : "Created user successfully"}), 201
    
@app.route('/users', methods=["GET"])
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

@app.route('/users/<int:id>', methods=["GET"])
def get_one_user(id):
    user = User.query.filter_by(id=id).first()
    
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
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({"msg" : "User not found"}), 401
    
    data = request.get_json()

    user.name = data["name"]
    user.email = data["email"]

    db.session.commit()
    
    return jsonify({"user" : "User has been updated"}), 201

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_one_user(id):
    user = User.query.filter_by(id=id).first()

    if not user:
        return jsonify({"msg" : "User not found"}), 401
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({"msg" : "User has been deleted"}), 201


@app.route('/login', methods=["POST"])
def user_login():
    data = request.get_json()
    selected_user = User.query.filter_by(email=data["email"]).first()
    if selected_user:
        if not check_password_hash(selected_user.password, data["password"]):
            return jsonify({"msg" : "Invalid password"}), 404
        return jsonify({"msg" : "Login successfully"}), 201

    return jsonify({"msg" : "Invalid email"}), 404


