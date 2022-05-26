from datetime import datetime, timedelta
from functools import wraps
import json
from types import MethodDescriptorType
import uuid ,jwt
from winreg import QueryReflectionKey
from multiprocessing import AuthenticationError
from flaskr.model import Arrange_Sentences_Answer_Choices_Class, Arrange_sentences, Lessons, Lessons_Content, Material_Content_Class, Materials, Multiple_Choices_Answers_Class, Multiple_choices, Questions_Class, Quizzes, Short_answers, Users, Children, db
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
            data = jwt.decode(token, secret, algorithms='HS256')
            current_user = Users.query.filter_by(id = data['id']).first()
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
    
    new_user = Users(name=data['name'], email=data['email'], encode_password=data['password'], pin=0)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"msg" : "Created user successfully"}), 201
    
@app.route('/users', methods=["GET"])
@token_required
def get_all_user(current_user):
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
@token_required
def get_one_Users(current_user, id):
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
@token_required
def update_one_user(current_user, id):
    user = Users.query.filter_by(id=id).first()
    if not user:
        return jsonify({"msg" : "User not found"}), 401
    
    data = request.get_json()

    user.name = data["name"]
    user.email = data["email"]

    db.session.commit()
    
    return jsonify({"user" : "User has been updated"}), 201

@app.route('/users/<int:id>', methods=['DELETE'])
@token_required
def delete_one_user(current_user, id):
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
            'id': selected_user.id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, secret, algorithm="HS256")
        return jsonify({'token' : token}), 201

    return jsonify({"msg" : "Invalid password"}), 404

@app.route('/users/pin', methods=["POST"])
@token_required
def add_pin(current_user):
    data = request.get_json()
    selected_user = Users.query.filter_by(email=data["email"]).first()
    
    if selected_user.pin != 0:
        return jsonify({"msg" : "User already have pin"})
    
    selected_user.pin = data["pin"]
    db.session.commit()
    
    return jsonify({'msg' : 'Pin added successfully'})

@app.route('/users/pin/check', methods=['POST'])
@token_required
def check_pin(current_user):
    data = request.get_json()
    selected_user = Users.query.filter_by(email=data["email"]).first()
    
    if selected_user != 0:
        return jsonify({"msg" : "user already have pin"})
    
    return jsonify({"msg" : "user don't have pin"})

@app.route('/users/<int:id>/children', methods=["POST"])
@token_required
def add_children(current_user, id):
    data = request.get_json()
    new_children = Children(name=data['name'], level=0, Users_id=id)
    
    db.session.add(new_children)
    db.session.commit()
    
    return jsonify({"msg" : "Created children successfully"}), 201

@app.route('/users/<int:id>/children', methods=['GET'])
@token_required
def get_all_children(current_user, id):

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
@token_required
def get_one_children(current_user, children_id, id):
    children = Children.query.filter_by(id=children_id, Users_id=id).first()
    if not children:
        return jsonify({"msg" : "Children not found"}), 401
    
    children_data = {}
    children_data['id'] = children.id
    children_data['name'] = children.name
    children_data['level'] = children.level
    
    return jsonify({"user" : children_data})


@app.route('/users/<int:id>/children/<int:children_id>', methods=['PUT'])
@token_required
def update_one_children(current_user, children_id, id):
    selected_children = Children.query.filter_by(id=children_id, Users_id=id).first()
    if not selected_children:
        return jsonify({"msg" : "Children not found"}), 401
    
    data = request.get_json()

    selected_children.name = data["name"]

    db.session.commit()
    
    return jsonify({"user" : "Children has been updated"}), 201


@app.route('/users/<int:id>/children/<int:children_id>', methods=['DELETE'])
@token_required
def delete_one_children(current_user, children_id, id):
    children = Children.query.filter_by(id=children_id, Users_id=id).first()

    if not children:
        return jsonify({"msg" : "Children not found"}), 401
    
    db.session.delete(children)
    db.session.commit()
    
    return jsonify({"msg" : "Children has been deleted"}), 201


@app.route('/lessons', methods=['GET'])
@token_required
def get_lesson(current_user):
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
@token_required
def get_lessons_content(current_user, id):
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
        lessons_content_data['Materials_id'] = lessons_content.Materials_id
        lessons_content_data['Quizzes_id'] = lessons_content.Quizzes_id
        
        all_lessons_content.append(lessons_content_data)
    
    return jsonify({"Lessons content" : all_lessons_content})


@app.route('/materials/<int:id>', methods=['GET'])
@token_required
def get_materials_content_by_id(current_user, id):
    query = Material_Content_Class.query.filter_by(Materials_id=id)
    
    all_materials_content = []
    
    for materials_content in query:
        materials_content_data = {}
        materials_content_data['order'] = materials_content.order
        materials_content_data['text'] = materials_content.text
        materials_content_data['image'] = materials_content.image
        materials_content_data['audio'] = materials_content.audio
        
        all_materials_content.append(materials_content_data)
    
    return jsonify({"materials content" : all_materials_content})


@app.route('/quizzes/<int:id>', methods=['GET'])
@token_required
def get_all_questions_by_quizzes_id(current_user, id):
    query = Questions_Class.query.filter_by(Quizzes_id=id)
    
    all_questions = []
    
    for questions in query:
        questions_data = {}
        questions_data['order'] = questions.order
        questions_data['type'] = questions.type
        
        all_questions.append(questions_data)
    
    return jsonify({"materials content" : all_questions})


@app.route('/questions/<int:question_id>', methods=['GET'])
@token_required
def get_questions_by_question_type(current_user, question_id):
    query = Questions_Class.query.filter_by(id=question_id).first()

    if not query:
        return jsonify({"msg" : "Questions not found"}), 401
    
    all_questions_data = []
    
    questions_data = {}
    questions_data['order'] = query.order
    questions_data['type'] = query.type
    # all_questions_data.append(questions_data)
    
    if query.type == 0:
        query_short_answer = Multiple_choices.query.filter_by(id=question_id).first()

        questions_data['type'] = {
            'multiple_choice_text' : query_short_answer.q_text,
            'multiple_choice_image' : query_short_answer.q_image,
            'multiple_choice_audio' : query_short_answer.q_audio,
            'answer' : query_short_answer.answer
        }
        
        query_answer = Multiple_Choices_Answers_Class.query.filter_by(Multiple_Choices_id=query_short_answer.id)
        
        all_questions_data.append(questions_data)
        
        for answer in query_answer:
            questions_data['type']['answer'] = {
                'answer_choice' : answer.choice,
                'answer_text' : answer.text,
                'answer_audio' : answer.audio,
                'answer_image' : answer.image
            }
        
    elif query.type == 1:
        query_arrange_sentences= Arrange_sentences.query.filter_by(id=question_id).first()
        questions_data['type'] = {
            'arrange_sentences_text' : query_arrange_sentences.q_text,
            'arrange_sentences_image' : query_arrange_sentences.q_image,
            'arrange_sentences_audio' : query_arrange_sentences.q_audio,
            'answer' : query_arrange_sentences.answer
        }
        
        query_answer = Arrange_Sentences_Answer_Choices_Class.query.filter_by(Arrange_Sentences_id=query_arrange_sentences.id)
        
        for answer in query_answer:
            questions_data['type']['answer'] = {
                'word' : answer.word
            }

    else:
        query_short_answer = Short_answers.query.filter_by(id=question_id).first()
        questions_data['type'] = {
            'short_answer_type' : query_short_answer.type,
            'short_answer_text' : query_short_answer.q_text,
            'short_answer_image' : query_short_answer.q_image,
            'short_answer_audio' : query_short_answer.q_audio,
            'answer' : query_short_answer.answer
        }
        
    all_questions_data.append(questions_data)

    return jsonify({"questions" : all_questions_data})

    