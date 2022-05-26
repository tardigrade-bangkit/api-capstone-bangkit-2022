from calendar import c
from enum import unique
from secrets import choice
from flaskr.__init__ import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flaskr.__init__ import db
import random
from datetime import datetime

NUMBERS = ['0','1','2','3','4','5','6','7','8','9']

class Users(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(length=50), unique=True, nullable=False)
    password = db.Column(db.String(length=20), nullable=False)
    name = db.Column(db.String(length=50), unique=False, nullable=False)
    pin = db.Column(db.String(length=6), unique=False, nullable=False)
    
    ## one to many = users - children
    children = db.relationship('Children', backref="users_children", lazy=True)
    
    ## one to many = avatars - users
    Avatars_id = db.Column(db.Integer, db.ForeignKey('avatars.id'))
    
    @property
    def encode_password(self):
        return self.encode_password
    
    @encode_password.setter
    def encode_password(self, password_to_hash):
        self.password = bcrypt.generate_password_hash(password_to_hash).decode("utf-8")
    
    # @property
    # def encode_pin(self):
    #     return self.encode_pin
    
    # @encode_pin
    # def encode_pin(self, pin_to_hash):
    #     self.pin = bcrypt.generate_password_hash(pin_to_hash).decode("utf-8")


class Avatars(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(length=255), nullable=False)
    
    users = db.relationship('Users', backref='avatar_users', lazy=True)
    children = db.relationship("Children", backref='avatar_children', lazy=True)
    

class Usages(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    time_start = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time_end = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    Children_id = db.Column(db.Integer, db.ForeignKey('children.id'))
 
class Progress_Association(db.Model):
    __tablename__ = 'Progress'
    __table_args__ = {'extend_existing': True}
    progress = db.Column(db.Integer, nullable=False)
    Children_id = db.Column(db.Integer, db.ForeignKey('children.id'), primary_key=True)
    Lessons_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), primary_key=True)
    
    children = db.relationship("Children", back_populates="lessons")
    lessons = db.relationship("Lessons", back_populates="children")

class Children_Badges_Association(db.Model):
    __tablename__ = 'Children_Badges'
    __table_args__ = {'extend_existing': True}
    acquired_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Children_id = db.Column(db.Integer, db.ForeignKey('children.id'), primary_key=True)
    Badges_id = db.Column(db.Integer, db.ForeignKey('badges.id'), primary_key=True)
    
    children = db.relationship("Children", back_populates="badges")
    badges = db.relationship("Badges", back_populates="children")
    
class Children_Missions_Association(db.Model):
    __tablename__ = "Children_Missions"
    __table_args__ = {'extend_existing' : True}
    status = db.Column(db.Integer, nullable=False)
    active_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    finish_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Children_id = db.Column(db.Integer, db.ForeignKey('children.id'), primary_key=True)
    Missions_id = db.Column(db.Integer, db.ForeignKey('missions.id'), primary_key=True)
    
    children = db.relationship("Children", back_populates="missions")
    missions = db.relationship("Missions", back_populates="children")
    
class Children_Achievements_Association(db.Model):
    __tablename__ = 'Children_Achievements'
    __table_args__ = {'extend_existing': True}
    acquired_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Children_id = db.Column(db.Integer, db.ForeignKey('children.id'), primary_key=True)
    Achievements_id = db.Column(db.Integer, db.ForeignKey('achievements.id'), primary_key=True)
    
    children = db.relationship("Children", back_populates="achievements")
    achievements = db.relationship("Achievements", back_populates="children")

class Children(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), unique=False, nullable=False)
    level = db.Column(db.Integer, unique=False, nullable=False)
    Users_id  = db.Column(db.Integer, db.ForeignKey("users.id"))
    Avatars_id = db.Column(db.Integer, db.ForeignKey("avatars.id"))

    usages = db.relationship('Usages', backref='children', lazy=True)
    badges = db.relationship('Children_Badges_Association', back_populates="children")
    achievements = db.relationship('Children_Achievements_Association', back_populates="children")
    lessons = db.relationship('Progress_Association', back_populates="children")
    missions = db.relationship('Children_Missions_Association', back_populates="children")
    
class Achievements(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=255), nullable=False)
    description = db.Column(db.String(length=255), nullable=False)
    image_url = db.Column(db.String(length=255), nullable=False)
    children = db.relationship('Children_Achievements_Association', back_populates="achievements")

class Missions(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=255), )
    type = db.Column(db.Integer, nullable=False)
    c_duration = db.Column(db.Integer, nullable=False)
    c_min_score = db.Column(db.Integer, nullable=False)
    Lessons_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))
    
    children = db.relationship('Children_Missions_Association', back_populates="missions")


class Badges(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(length=100), nullable=False)
    children = db.relationship('Children_Badges_Association', back_populates="badges")
    lessons = db.relationship('Lessons', backref="badges", uselist=False) # one to one 
    
class Lessons(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    cover_image = db.Column(db.String(length=100), unique=False, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(length=100), unique=False, nullable=False)
    type = db.Column(db.String(length=100), nullable=False)
    Badges_id = db.Column(db.Integer, db.ForeignKey('badges.id')) # one to one
    
    children = db.relationship('Progress_Association', back_populates="lessons") # many to many
    missions = db.relationship('Missions', backref='lessons', lazy=True)
    lessons_content = db.relationship('Lessons_Content', backref='lessons', lazy=True) # one to many
    
class Lessons_Content(db.Model):
    __tablename__ = 'Lessons_Content'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(length=100), nullable=False)
    Lessons_id = db.Column(db.Integer, db.ForeignKey('lessons.id')) # many to one
    Materials_id = db.Column(db.Integer, db.ForeignKey('materials.id'))
    Quizzes_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    
class Materials(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    lessons_content = db.relationship('Lessons_Content', backref="materials", uselist=False) # one to one
    material_content = db.relationship('Material_Content_Class', backref='materials', lazy=True)
    
class Material_Content_Class(db.Model):
    __tablename__ = 'Material_Content'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(length=255), nullable=False)
    image = db.Column(db.String(length=255), nullable=False)
    audio = db.Column(db.String(length=255), nullable=False)
    Materials_id = db.Column(db.Integer, db.ForeignKey('materials.id'))
    
class Quizzes(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    lessons_content = db.relationship('Lessons_Content', backref="quizzes", uselist=False) # one to one
    questions = db.relationship('Questions_Class', backref='quizzes', lazy=True)
    
class Questions_Class(db.Model):
    __tablename__ = 'Questions'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    Quizzes_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    Multiple_choices_id = db.Column(db.Integer, db.ForeignKey('multiple_choices.id'))
    Arrange_Sentences_id = db.Column(db.Integer, db.ForeignKey('arrange_sentences.id'))
    Short_Answers_id = db.Column(db.Integer, db.ForeignKey('short_answers.id'))
    

class Multiple_choices(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    q_text = db.Column(db.String(length=255), nullable=False)
    q_audio = db.Column(db.String(length=255), nullable=False)
    q_image = db.Column(db.String(length=255), nullable=False)
    answer = db.Column(db.String(length=1), nullable=False)
    questions = db.relationship('Questions_Class', backref="multiple_choices", uselist=False) # one to one
    multiple_choices_answer = db.relationship('Multiple_Choices_Answers_Class', backref="multiple_choices", lazy=True)


class Multiple_Choices_Answers_Class(db.Model):
    __tablename__ = 'Multiple_Choices_Answers'
    __table_args__ = {'extend_existing': True}
    choice = db.Column(db.String(length=1), nullable=False)
    text = db.Column(db.Integer, nullable=True)
    audio = db.Column(db.Integer, nullable=True)
    image = db.Column(db.Integer, nullable=True)
    Multiple_Choices_id = db.Column(db.Integer, db.ForeignKey('multiple_choices.id'), primary_key=True)
    
class Arrange_sentences(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    q_text = db.Column(db.String(length=255), nullable=True)
    q_audio = db.Column(db.String(length=255), nullable=True)
    q_image = db.Column(db.String(length=255), nullable=True)
    answer = db.Column(db.String(length=255), nullable=False)
    questions = db.relationship('Questions_Class', backref="arrange_sentences", uselist=False) # one to one
    arrange_sentences_answer_choices = db.relationship('Arrange_Sentences_Answer_Choices_Class', backref="arrange_sentences", lazy=True)

    
class Arrange_Sentences_Answer_Choices_Class(db.Model):
    __tablename__ = 'Arrange_Sentences_Answer_Choices'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(length=255), nullable=False)
    Arrange_Sentences_id = db.Column(db.Integer, db.ForeignKey('arrange_sentences.id'))

    
class Short_answers(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(length=255), nullable=False)
    answer = db.Column(db.String(length=255), nullable=False)
    q_text = db.Column(db.String(length=255), nullable=False)
    q_audio = db.Column(db.String(length=255), nullable=False)
    q_image = db.Column(db.String(length=255), nullable=False)
    questions = db.relationship('Questions_Class', backref="short_answers", uselist=False) # one to one

    