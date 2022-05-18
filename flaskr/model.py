from secrets import choice
from flaskr.__init__ import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flaskr.__init__ import db
import random

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(length=50), unique=True, nullable=False)
    password = db.Column(db.String(length=20), nullable=False)
    name = db.Column(db.String(length=50), unique=False, nullable=False)
    pin = db.Column(db.String(length=6), unique=True, nullable=False)
    
    ## one to many = users - children
    children = db.relationship('Children', backref="users", lazy=True)
    
    ## one to many = avatars - users
    Avatars_id = db.Column(db.Integer, db.ForeignKey('avatars.id'))
    
    @property
    def encode_password(self):
        return self.encode_password
    
    @encode_password.setter
    def encode_password(self, password_to_hash):
        self.password = bcrypt.generate_password_hash(password_to_hash).decode("utf-8")
    
    
    def get_random_pin(self):
        list_pin=[]
        fix_pin=""
        for _ in range(6):
            list_pin.append(random.choice(NUMBERS))
        for number in list_pin:
            fix_pin+=number
        return fix_pin
    
    @property
    def generate_pin(self):
        return self.generate_pin
    
    @generate_pin.setter
    def generate_pin(self):
        self.pin = self.get_random_pin()


class Avatars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(length=100), nullable=False)
    
    users = db.relationship('Users', backref='avatar', lazy=True)
    
#Many to Many between children and lessons     
Progress = db.Table('Progress',
    db.Column('id_children', db.Integer, db.ForeignKey('children.id'), primary_key=True),
    db.Column('id_lessons', db.Integer, db.ForeignKey('lessons.id'), primary_key=True)
)
class Children(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), unique=False, nullable=False)
    id_avatar = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)


    lesson = db.relationship('Lessons', secondary=Progress, backref='childrens', lazy=True)
    ## one to many = children -> children achievement
    children_achievements = db.relationship('Children_Achievements', backref="children", lazy=True)
    ## one to many = users - children
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    
## one to many - lessons -> lesson_content
## many to many - children -> lessons
class Lessons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cover_image = db.Column(db.LargeBinary, unique=False, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(length=100), unique=False, nullable=False)
    type = db.Column(db.String(length=100), nullable=False)
    ## one to many = lessons -> lessons_content
    lesson_content = db.relationship('Lesson_Content', backref="lessons", lazy=True)
    
class Lesson_Content(db.Model):
    order = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, nullable=False)
    
    ## one to many = lessons -> lessons_content
    lessons_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))

class Children_Achievements(db.Model):
    acquired_date = db.Column(db.Integer, nullable=False)
    ## one to many = children -> children_achievements
    children_id = db.Column(db.Integer, db.ForeignKey('children.id'))
    
class Achievements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(length=100), nullable=False)

class Children_Badgets(db.Model):
    acquired_date = db.Column(db.Integer, nullable=False)
    ## one to many = children -> children_badges
    children_id = db.Column(db.Integer, db.ForeignKey('children.id'))
    
    ## one to many = badges -> children_badges
    badges = db.relationship('Badges', backref="children_badgets", lazy=True)

class Badges(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(length=100), nullable=False)

    ## one to many = badges -> children_badges
    children_badgets_id = db.Column(db.Integer, db.ForeignKey('children_badgets.acquired_date'))
    
    
class Materials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    material_content = db.relationship('Material_Content', backref='materials', lazy=True)
    
class Material_Content(db.Model):
    order = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(length=255), nullable=False)
    image = db.Column(db.String(length=255), nullable=False)
    audio = db.Column(db.String(length=255), nullable=False)
    Materials_id = db.Column(db.Integer, db.ForeignKey('materials.id'))

class Multiple_Choices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q_text = db.Column(db.String(length=255), nullable=False)
    q_audio = db.Column(db.String(length=255), nullable=False)
    q_image = db.Column(db.String(length=255), nullable=False)
    answer = db.Column(db.String(length=1), nullable=False)
    multiple_choices_answers = db.relationship("Multiple_Choices_Answers", backref="multiple_choices", lazy=True)
    
class Multiple_Choices_Answers(db.Model):
    choice = db.Column(db.String(length=1), nullable=False)
    text = db.Column(db.Integer, nullable=True)
    audio = db.Column(db.Integer, nullable=True)
    image = db.Column(db.Integer, nullable=True)
    Multiple_Choices_id = db.Column(db.Integer, db.ForeignKey('multiple_choices.id'))
    
class Arrange_Sentences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q_text = db.Column(db.String(length=255), nullable=True)
    q_audio = db.Column(db.String(length=255), nullable=True)
    q_image = db.Column(db.String(length=255), nullable=True)
    answer = db.Column(db.String(length=255), nullable=False)
    
class Arrange_Sentences_Answer_Choices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(length=255), nullable=False)
    Arrange_Sentences_id = db.Column(db.Integer, db.ForeignKey('arrange_sentences.id'))

    
class Short_Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_camera = db.Column(db.Boolean, nullable=False)
    answer = db.Column(db.String(length=255), nullable=False)
    q_text = db.Column(db.String(length=255), nullable=False)
    q_audio = db.Column(db.String(length=255), nullable=False)
    q_image = db.Column(db.String(length=255), nullable=False)
    