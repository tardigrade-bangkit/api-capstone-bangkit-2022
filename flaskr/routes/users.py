from datetime import datetime, timedelta
import random, string
from functools import wraps
import base64
import logging
from types import MethodDescriptorType
import uuid
import jwt
from multiprocessing import AuthenticationError
from flaskr.model import Achievements, Avatars, Children_Badges_Association, Missions, Arrange_Sentences_Answer_Choices_Class, Arrange_sentences, Badges, Children_Achievements_Association, Children_Missions_Association, Lessons, Lessons_Content, Material_Content_Class, Materials, Missions, Multiple_Choices_Answers_Class, Multiple_choices, Progress, Questions_Class, Quizzes, Short_answers, Usages, Users, Children, db
from flaskr.__init__ import app, secret
from flask import jsonify, request
from flask_bcrypt import check_password_hash
# from flaskr.model import main

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'msg': 'Token is missing !!'}), 401

        current_user = None
        try:
            data = jwt.decode(token, secret, algorithms='HS256')
            current_user = Users.query.filter_by(id=data['id']).first()
        except Exception as e:
            logging.exception(e)

        if not current_user:
            return jsonify({
                'msg': 'Token is invalid'
            }), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/users', methods=["POST"])
def add_user():

    data = request.get_json()
    selected_email = Users.query.filter_by(email=data["email"]).first()
    if selected_email:
        return jsonify({"msg": "User already taken, try with another email!"}), 400

    new_user = Users(
        name=data['name'],
        email=data['email'],
        encode_password=data['password'],
        pin=0,
        Avatars_id=1,
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "Created user successfully"}), 201


@app.route('/users', methods=["GET"])
@token_required
def get_all_user(current_user):
    query = Users.query.join(Users.avatar_users).all()
    all_user = []

    for user in query:
        user_data = {}
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['email'] = user.email
        user_data['avatar'] = user.avatar_users.image_url

        all_user.append(user_data)

    return jsonify({"users": all_user})


@app.route('/users/<int:id>', methods=["GET"])
@token_required
def get_one_Users(current_user, id):
    user = Users.query.filter_by(id=id).first()

    if not user:
        return jsonify({"msg": "User not found"}), 401

    user_data = {}
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['email'] = user.email

    return jsonify({"user": user_data})


@app.route('/users/self', methods=["GET"])
@token_required
def get_self(current_user):
    avatar = Avatars.query.filter_by(id=current_user.Avatars_id).first()

    user_data = {
        'id': current_user.id,
        'name': current_user.name,
        'email': current_user.email,
        'has_pin': current_user.pin != "0",
        'avatar': avatar.image_url
    }

    return jsonify({"user": user_data})


@app.route('/users/<int:id>', methods=['PUT'])
@token_required
def update_one_user(current_user, id):
    user = Users.query.filter_by(id=id).first()
    if not user:
        return jsonify({"msg": "User not found"}), 401

    data = request.get_json()

    user.name = data["name"]
    user.email = data["email"]

    db.session.commit()

    return jsonify({"user": "User has been updated"}), 201


@app.route('/users/<int:id>', methods=['DELETE'])
@token_required
def delete_one_user(current_user, id):
    user = Users.query.filter_by(id=id).first()

    if not user:
        return jsonify({"msg": "User not found"}), 401

    db.session.delete(user)
    db.session.commit()

    return jsonify({"msg": "User has been deleted"}), 201


@app.route('/login', methods=["POST"])
def user_login():
    data = request.get_json()
    selected_user = Users.query.filter_by(email=data["email"]).first()

    if not selected_user:
        return jsonify({"msg": "Invalid authorization "}), 404

    if check_password_hash(selected_user.password, data["password"]):
        token = jwt.encode({
            'id': selected_user.id
        }, secret, algorithm="HS256")
        return jsonify({
            'token': token,
            'has_pin': selected_user.pin != "0"
        }), 201

    return jsonify({"msg": "Invalid password"}), 404


@app.route('/pin', methods=["POST"])
@token_required
def add_pin(current_user):
    data = request.get_json()

    if current_user.pin != "0":
        return jsonify({"msg": "User already have pin"}), 400

    current_user.pin = data["pin"]
    db.session.commit()

    return jsonify({"msg": "Pin added successfully"})


@app.route('/pin/check', methods=['POST'])
@token_required
def check_pin(current_user):
    data = request.get_json()

    if current_user.pin == "0":
        return jsonify({"msg": "User don't have pin"}), 400

    if (data["pin"] != current_user.pin):
        return jsonify({"msg": "Incorrect pin"}), 400

    return jsonify({"msg": "Correct pin"})


@app.route('/children', methods=["POST"])
@token_required
def add_children(current_user):
    data = request.get_json()

    new_children = Children(
        name=data['name'],
        level=0,
        Users_id=current_user.id,
        Avatars_id=data['avatar'],
        tgl_lahir=datetime.strptime(data["birthdate"], '%d/%m/%Y')
    )

    db.session.add(new_children)
    db.session.commit()

    return jsonify({
        "new_child": {
            'id': new_children.id,
            'name': new_children.name,
            'level': new_children.level,
            'avatar': new_children.avatar_children.image_url,
            'birthdate': new_children.tgl_lahir
        }
    }), 201


@app.route('/children', methods=['GET'])
@token_required
def get_all_children(current_user):

    query = Children.query.filter_by(Users_id=current_user.id).join(
        Children.avatar_children).all()
    all_children = []

    for children in query:
        children_data = {}
        children_data['id'] = children.id
        children_data['name'] = children.name
        children_data['level'] = children.level
        children_data['avatar'] = children.avatar_children.image_url
        children_data['birthdate'] = children.tgl_lahir.strftime('%d/%m/%Y')

        all_children.append(children_data)

    return jsonify({"children": all_children})


@app.route('/children/<int:children_id>', methods=['GET'])
@token_required
def get_one_children(current_user, children_id, id):
    children = Children.query.filter_by(id=children_id, Users_id=id).first()
    if not children:
        return jsonify({"msg": "Children not found"}), 401

    children_data = {}
    children_data['id'] = children.id
    children_data['name'] = children.name
    children_data['level'] = children.level

    return jsonify({"user": children_data})


@app.route('/children/<int:children_id>', methods=['PUT'])
@token_required
def update_one_children(current_user, children_id):
    selected_children = Children.query.filter_by(
        id=children_id, Users_id=current_user.id).first()
    if not selected_children:
        return jsonify({"msg": "Children not found"}), 401

    data = request.get_json()

    selected_children.level = data["level"]

    db.session.commit()

    return jsonify({"user": "Children has been updated"}), 201


@app.route('/children/<int:children_id>', methods=['DELETE'])
@token_required
def delete_one_children(current_user, children_id, id):
    children = Children.query.filter_by(id=children_id, Users_id=id).first()

    if not children:
        return jsonify({"msg": "Children not found"}), 401

    db.session.delete(children)
    db.session.commit()

    return jsonify({"msg": "Children has been deleted"}), 201


@app.route('/lessons/<int:level>', methods=['GET'])
@token_required
def get_lesson(current_user, level):
    query = Lessons.query.filter_by(level=level)

    if not query:
        return jsonify({"msg": "Lessons not found"})

    lessons_data = []

    for lessons in query:
        list_lessons = {}
        list_lessons['id'] = lessons.id
        list_lessons['title'] = lessons.title
        list_lessons['cover_image'] = lessons.cover_image
        list_lessons['type'] = lessons.type

        lessons_data.append(list_lessons)

    return jsonify({"lessons": lessons_data})


@app.route('/lessons/content/<int:id>', methods=['GET'])
@token_required
def get_lessons_content(current_user, id):
    selected_lessons = Lessons_Content.query.filter_by(
        Lessons_id=id).order_by(Lessons_Content.order.asc())

    if not selected_lessons:
        return jsonify({"msg": "Lessons not found"}), 401

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

    return jsonify({"lesson_contents": all_lessons_content})


@app.route('/materials/<int:id>', methods=['GET'])
@token_required
def get_materials_content_by_id(current_user, id):
    query = Material_Content_Class.query.filter_by(
        Materials_id=id).order_by(Material_Content_Class.order.asc())

    all_materials_content = []

    for materials_content in query:
        materials_content_data = {}
        materials_content_data['order'] = materials_content.order
        materials_content_data['text'] = materials_content.text
        materials_content_data['image'] = materials_content.image
        materials_content_data['audio'] = materials_content.audio

        all_materials_content.append(materials_content_data)

    return jsonify(all_materials_content)


@app.route('/quizzes/<int:id>', methods=['GET'])
@token_required
def get_all_questions_by_quizzes_id(current_user, id):
    quiz = Quizzes.query.filter_by(id=id)
    query = Questions_Class.query.filter_by(
        Quizzes_id=id).order_by(Questions_Class.order.asc())

    quiz_data = {}
    # quiz_data['is_final'] = quiz.is_final
    quiz_data['questions'] = []

    for questions in query:
        questions_data = {}
        questions_data['order'] = questions.order
        questions_data['type'] = questions.type
        questions_data['multiple_choices_id'] = questions.Multiple_choices_id
        questions_data['arrange_words_id'] = questions.Arrange_Sentences_id
        questions_data['short_answer_id'] = questions.Short_Answers_id
        questions_data['id'] = questions.id

        quiz_data['questions'].append(questions_data)

    return jsonify(quiz_data)


@app.route('/questions/<int:question_id>', methods=['GET'])
@token_required
def get_questions_by_question_type(current_user, question_id):
    query = Questions_Class.query.filter_by(id=question_id).first()

    if not query:
        return jsonify({"msg": "Questions not found"}), 401

    questions_data = {}
    questions_data['order'] = query.order
    questions_data['type'] = query.type

    if query.type == 0:
        multiple_choices = Multiple_choices.query.filter_by(
            id=query.Multiple_choices_id).first()

        query_answer = Multiple_Choices_Answers_Class.query.filter_by(
            Multiple_Choices_id=multiple_choices.id)
        questions_data['question_text'] = multiple_choices.q_text
        questions_data['question_image'] = multiple_choices.q_image
        questions_data['question_audio'] = multiple_choices.q_audio
        questions_data['answer'] = multiple_choices.answer

        questions_data['answer_choices'] = []

        for answer in query_answer:
            answer_choice = {
                'answer_choice': answer.choice,
                'answer_text': answer.text,
                'answer_audio': answer.audio,
                'answer_image': answer.image
            }
            questions_data['answer_choices'].append(answer_choice)

    elif query.type == 1:
        query_arrange_sentences = Arrange_sentences.query.filter_by(
            id=query.Arrange_Sentences_id).first()

        questions_data['question_text'] = query_arrange_sentences.q_text
        questions_data['question_image'] = query_arrange_sentences.q_image
        questions_data['question_audio'] = query_arrange_sentences.q_audio
        questions_data['answer'] = query_arrange_sentences.answer

        query_answer = Arrange_Sentences_Answer_Choices_Class.query.filter_by(
            Arrange_Sentences_id=query_arrange_sentences.id)

        questions_data['answer_words'] = []

        for answer in query_answer:
            questions_data['answer_words'].append(answer.word)

    elif query.type == 2:
        query_short_answer = Short_answers.query.filter_by(
            id=query.Short_Answers_id).first()

        questions_data['short_answer_type'] = query_short_answer.type
        questions_data['question_text'] = query_short_answer.q_text
        questions_data['question_image'] = query_short_answer.q_image
        questions_data['question_audio'] = query_short_answer.q_audio
        questions_data['answer'] = query_short_answer.answer

    else:
        return jsonify({"msg", "type invalid"}), 400
    return jsonify(questions_data)


@app.route('/achievements', methods=['GET'])
@token_required
def get_all_achievements(current_user):
    query = Achievements.query.all()
    all_achievements = []

    for achievments in query:
        achievments_data = {}
        achievments_data['id'] = achievments.id
        achievments_data['description'] = achievments.description
        achievments_data['name'] = achievments.name
        achievments_data['image_url'] = achievments.image_url

        all_achievements.append(achievments_data)

    return jsonify({"achievements": all_achievements})


@app.route('/achievements/<int:child_id>', methods=['GET'])
@token_required
def get_all_achievements_of_children(current_user, child_id):
    query_achievements = Children_Achievements_Association.query.filter_by(
        Children_id=child_id).join(Children_Achievements_Association.achievements).all()

    all_achievements = []
    len_data = len(query_achievements)

    for i in range(0, len_data):
        data = {
            'id': query_achievements[i].achievements.id,
            'description': query_achievements[i].achievements.description,
            'name': query_achievements[i].achievements.name,
            'image_url': query_achievements[i].achievements.image_url,
            'acquired_date': query_achievements[i].acquired_date.strftime("%Y/%m/%d %H:%M:%S")
        }

        all_achievements.append(data)

    return jsonify({"achievements": all_achievements})


@app.route('/achievements/<int:achievements_id>', methods=['POST'])
@token_required
def add_children_achievement(current_user, achievements_id):
    data = request.get_json()
    selected_children_achievements = Children_Achievements_Association.query.filter_by(
        Children_id=data['Children_id']).all()

    check_achievements = Achievements.query.filter_by(
        id=achievements_id).first()
    if not check_achievements:
        return jsonify({"msg": "Achievements doesn't exist"})

    check_chidren = Children.query.filter_by(id=data['Children_id']).first()
    if not check_chidren:
        return jsonify({"msg": "Children not exist"})

    for i in range(0, len(selected_children_achievements)):
        if (achievements_id == selected_children_achievements[i].Achievements_id):
            return jsonify({"msg": "Cannot take same achievements"})

    new_children_achievements = Children_Achievements_Association(
        acquired_date=datetime.utcnow(), Achievements_id=achievements_id, Children_id=data['Children_id'])

    db.session.add(new_children_achievements)
    db.session.commit()

    return jsonify({"msg": "Children achievement added successfully"}), 201


@app.route('/missions', methods=['GET'])
@token_required
def get_all_missions(current_user):
    query = Missions.query.all()
    all_missions = []

    for missions in query:
        missions_data = {}
        missions_data['id'] = missions.id
        missions_data['title'] = missions.title
        missions_data['type'] = missions.type
        missions_data['c_duration'] = missions.c_duration
        missions_data['c_min_score'] = missions.c_min_score

        all_missions.append(missions_data)

    return jsonify({"missions": all_missions})


@app.route('/missions/<int:id>', methods=['GET'])
@token_required
def get_all_missions_of_children(current_user, id):
    query_missions = Missions.query.join(
        Missions.children).filter_by(Children_id=id).all()

    all_missions = []
    len_data = len(query_missions)

    for i in range(0, len_data):
        data = {}
        data['id'] = query_missions[i].id
        data['title'] = query_missions[i].title
        data['type'] = query_missions[i].type
        data['c_duration'] = query_missions[i].c_duration
        data['c_min_score'] = query_missions[i].c_min_score

        all_missions.append(data)

    return jsonify({"missions": all_missions})


@app.route('/missions/<int:missions_id>', methods=['POST'])
@token_required
def add_children_missions(current_user, missions_id):
    data = request.get_json()
    selected_children_missions = Children_Missions_Association.query.filter_by(
        Children_id=data['Children_id']).all()

    check_missions = Missions.query.filter_by(id=missions_id).first()
    if not check_missions:
        return jsonify({"msg": "Missions doesn't exist"})

    check_chidren = Children.query.filter_by(id=data['Children_id']).first()
    if not check_chidren:
        return jsonify({"msg": "Children not exist"})

    for i in range(0, len(selected_children_missions)):
        if (missions_id == selected_children_missions[i].Missions_id):
            return jsonify({"msg": "Mission already taken"})

    new_children_missions = Children_Missions_Association(status=1, active_date=datetime.utcnow(
    ), finish_date=datetime.utcnow() + timedelta(minutes=30), Missions_id=missions_id, Children_id=data['Children_id'])

    db.session.add(new_children_missions)
    db.session.commit()

    return jsonify({"msg": "Children missions added successfully"}), 201


@app.route('/badges', methods=['GET'])
@token_required
def get_all_badges(current_user):
    query = Badges.query.all()
    all_badges = []

    for badges in query:
        badges_data = {}
        badges_data['id'] = badges.id
        badges_data['image_url'] = badges.image_url

        all_badges.append(badges_data)

    return jsonify({"badges": all_badges})


@app.route('/badges/<int:child_id>', methods=['GET'])
@token_required
def get_all_badges_of_children(current_user, child_id):
    query_badges = Children_Badges_Association.query.filter_by(
        Children_id=child_id).join(Children_Badges_Association.badges).all()

    all_badges = []
    len_data = len(query_badges)

    for i in range(0, len_data):
        data = {
            'id': query_badges[i].badges.id,
            'image_url': query_badges[i].badges.image_url,
            'acquired_date': query_badges[i].acquired_date.strftime("%Y/%m/%d %H:%M:%S")
        }

        all_badges.append(data)

    return jsonify({"badges": all_badges})


@app.route('/badges/<int:badges_id>', methods=['POST'])
@token_required
def add_children_badges(current_user, badges_id):
    data = request.get_json()
    selected_children_badges = Children_Badges_Association.query.filter_by(
        Children_id=data['Children_id']).all()

    check_badges = Badges.query.filter_by(id=badges_id).first()
    if not check_badges:
        return jsonify({"msg": "Badges doesn't exist"})

    check_chidren = Children.query.filter_by(id=data['Children_id']).first()
    if not check_chidren:
        return jsonify({"msg": "Children not exist"})

    for i in range(0, len(selected_children_badges)):
        if (badges_id == selected_children_badges[i].Badges_id):
            return jsonify({"msg": "Badges already taken"})

    new_children_badges = Children_Badges_Association(
        Badges_id=badges_id, Children_id=data['Children_id'])

    db.session.add(new_children_badges)
    db.session.commit()

    return jsonify({"msg": "Children badges added successfully"}), 201


@app.route('/lessons', methods=['GET'])
@token_required
def get_all_lessons(current_user):
    query = Lessons.query.all()
    all_lessons = []

    for lessons in query:
        lessons_data = {}
        lessons_data['id'] = lessons.id
        lessons_data['cover_image'] = lessons.cover_image
        lessons_data['level'] = lessons.level
        lessons_data['title'] = lessons.title
        lessons_data['type'] = lessons.type

        all_lessons.append(lessons_data)

    return jsonify({"lessons": all_lessons})


@app.route('/lessons/children/<int:id>', methods=['GET'])
@token_required
def get_all_lessons_of_children(current_user, id):
    query_lessons = Lessons.query.join(
        Lessons.children).filter_by(Children_id=id).all()

    all_lessons = []

    for i in range(0, len(query_lessons)):
        data = {}
        data['id'] = query_lessons[i].id
        data['cover_image'] = query_lessons[i].cover_image
        data['level'] = query_lessons[i].level
        data['title'] = query_lessons[i].title
        data['type'] = query_lessons[i].type

        all_lessons.append(data)

    return jsonify({"lessons": all_lessons})


@app.route('/usages/<int:children_id>', methods=['GET'])
@token_required
def get_all_usages_of_children(current_user, children_id):
    query = Usages.query.filter_by(Children_id=children_id).all()

    all_usages = []

    for i in range(0, len(query)):
        data = {}
        data['id'] = query[i].id
        data['time_start'] = query[i].time_start.strftime("%Y/%m/%d %H:%M:%S")
        data['time_end'] = query[i].time_end.strftime(
            "%Y/%m/%d %H:%M:%S") if query[i].time_end else None
        all_usages.append(data)

    return jsonify({"usages": all_usages})


@app.route('/usages/<int:children_id>', methods=['POST'])
@token_required
def add_usages_start(_, children_id):
    data = request.get_json()

    try:
        new_usages = Usages(time_start=datetime.strptime(
            data["time_start"], '%d/%m/%Y %H:%M:%S'), Children_id=children_id)
        db.session.add(new_usages)
        db.session.commit()

        return jsonify({"msg": "Usages start added successfully"}), 201
    except ValueError:
        return jsonify({"msg": "Date format is wrong"}), 400


@app.route('/usages/end/<int:children_id>', methods=['POST'])
@token_required
def add_usages_end(_, children_id):
    data = request.get_json()
    usages = Usages.query.filter_by(
        Children_id=children_id).order_by(Usages.id.desc()).first()

    if not usages:
        return jsonify({"msg": "Usages not exist"})

    try:
        time_end = datetime.strptime(data["time_end"], '%d/%m/%Y %H:%M:%S')

        if time_end < usages.time_start:
            return jsonify({"msg": "Time end is before time start"}), 400

        usages.time_end = datetime.strptime(
            data["time_end"], '%d/%m/%Y %H:%M:%S')
        db.session.commit()

        return jsonify({"msg": "Usages end added successfully"}), 200
    except ValueError:
        return jsonify({"msg": "Date format is wrong"}), 400


@app.route('/questions/multiple_choices/<int:answer_id>', methods=['GET'])
@token_required
def get_short_answer(current_user, answer_id):
    pass


# @app.route('/questions/arrange_sentences/<int:answer_id>', methods=['GET'])
# @token_required
# def get_short_answer(current_user, answer_id):
#     pass


# @app.route('/questions/short_answer/<int:answer_id>', methods=['GET'])
# @token_required
# def get_short_answer(current_user, answer_id):
#     pass
@app.route('/avatars', methods=['GET'])
def get_all_avatars():
    query = Avatars.query.all()
    all_avatars = []

    for avatars in query:
        avatars_data = {}
        avatars_data['id'] = avatars.id
        avatars_data['image_url'] = avatars.image_url

        all_avatars.append(avatars_data)

    return jsonify({"avatars": all_avatars})


@app.route('/progress/<int:child_id>', methods=['GET'])
@token_required
def get_all_progress_of_children(current_user, child_id):
    query_lessons = Progress.query.filter_by(Children_id=child_id).join(
        Progress.lessons).join(Progress.quizzes, isouter=True).all()

    all_lessons = []

    for i in range(0, len(query_lessons)):
        data = {
            'id': query_lessons[i].lessons.id,
            'title': query_lessons[i].lessons.title,
            'cover_image': query_lessons[i].lessons.cover_image,
            'finished_date': query_lessons[i].finished_date.strftime("%Y/%m/%d %H:%M:%S") if query_lessons[i].finished_date else None,
        }

        all_lessons.append(data)

    return jsonify({"lessons": all_lessons})


@app.route('/progress/<int:child_id>', methods=['POST'])
@token_required
def update_progress(current_user, child_id):
    data = request.get_json()
    selected_progress = Progress.query.filter_by(
        Children_id=child_id, Lessons_id=data['Lessons_id']).first()
    selected_lessons_content = Lessons_Content.query.filter_by(
        Lessons_id=data['Lessons_id']).all()

    if not selected_progress:
        return jsonify({"msg": "progess doesn't exist"})

    max_order = 0
    for i in range(0, len(selected_lessons_content)):
        if max_order < selected_lessons_content[i].order:
            max_order = selected_lessons_content[i].order

    if data['progress'] <= max_order and data['progress'] > selected_progress.progress:
        selected_progress.progress = data['progress']
        if data['progress'] == max_order:
            selected_progress.finished_date = datetime.utcnow()
    else:
        return jsonify({"msg": "progress invalid"}), 400

    db.session.commit()
    return jsonify({"msg": "progress updated successfully"})


# ANSWER

def isBase64(ans):
    try:
        return base64.b64encode(base64.b64decode(ans)) == ans
    except Exception:
        return False


@app.route('/quiz', methods=['POST'])
@token_required
def answer(current_user):
    data = request.get_json()

    correct_answer = 0

    for answer in data["list_answer"]:
        
        selected_questions = Questions_Class.query.filter_by(
            id=answer["question_id"]).first()

        if selected_questions.type == 0:
            get_id = selected_questions.Multiple_choices_id
            selected_answer = Multiple_choices.query.filter_by(
                id=get_id).first()

            if (answer["answer"] == selected_answer.answer):
                correct_answer += 1

        elif selected_questions.type == 1:
            get_id = selected_questions.Arrange_Sentences_id
            selected_answer = Arrange_sentences.query.filter_by(
                id=get_id).first()

            if (answer["answer"] == selected_answer.answer):
                correct_answer += 1

        elif selected_questions.type == 2:
            get_id = selected_questions.Short_Answers_id
            selected_answer = Short_answers.query.filter_by(id=get_id).first()

            if selected_answer.type == "audio":
                img_base64 = base64.decode(answer["answer"])
                string_list = string.ascii_lowercase
                result_name = ''.join(random.choice(string_list) for i in range(10))
                image_result = open(result_name, 'wb')
                image_result.write(img_base64)
                
            elif selected_answer.type == "image":
                img_base64 = base64.decode(answer["answer"])
                string_list = string.ascii_lowercase
                result_name = ''.join(random.choice(string_list) for i in range(10))
                image_result = open(result_name, 'wb')
                image_result.write(img_base64)
                
            elif selected_answer.type == "text":
                if (answer["answer"] == selected_answer.answer):
                    correct_answer += 1

        else:
            return jsonify({"msg", "invalid type"}), 400

    return jsonify({
        "correct_answer": correct_answer,
        "score": round((correct_answer / len(data["list_answer"])) * 100, 2)
    })
