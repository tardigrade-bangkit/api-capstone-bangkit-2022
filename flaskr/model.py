from calendar import c
from secrets import choice
from flaskr.__init__ import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flaskr.__init__ import db
import random

NUMBERS = ['0','1','2','3','4','5','6','7','8','9']

class Users(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(length=50), unique=True, nullable=False)
    password = db.Column(db.String(length=20), nullable=False)
    name = db.Column(db.String(length=50), unique=False, nullable=False)
    pin = db.Column(db.String(length=6), unique=True, nullable=False)
    
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
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(length=100), nullable=False)
    
    users = db.relationship('Users', backref='avatar_users', lazy=True)
    children = db.relationship("Children", backref='avatar_children', lazy=True)
    
    
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
    acquired_date = db.Column(db.Integer, nullable=False)
    Children_id = db.Column(db.Integer, db.ForeignKey('children.id'), primary_key=True)
    Badges_id = db.Column(db.Integer, db.ForeignKey('badges.id'), primary_key=True)
    
    children = db.relationship("Children", back_populates="badges")
    badges = db.relationship("Badges", back_populates="children")
    
class Children_Achievements_Association(db.Model):
    __tablename__ = 'Children_Achievements'
    __table_args__ = {'extend_existing': True}
    acquired_date = db.Column(db.Integer, nullable=False)
    Children_id = db.Column(db.Integer, db.ForeignKey('children.id'), primary_key=True)
    Achievements_id = db.Column(db.Integer, db.ForeignKey('achievements.id'), primary_key=True)
    
    children = db.relationship("Children", back_populates="achievements")
    achievements = db.relationship("Achievements", back_populates="children")

class Children(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), unique=False, nullable=False)
    level = db.Column(db.Integer, unique=False, nullable=False)
    Users_id  = db.Column(db.Integer, db.ForeignKey("users.id"))
    Avatars_id = db.Column(db.Integer, db.ForeignKey("avatars.id"))


    badges = db.relationship('Children_Badges_Association', back_populates="children")
    achievements = db.relationship('Children_Achievements_Association', back_populates="children")
    lessons = db.relationship('Progress_Association', back_populates="children")
    
class Lessons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cover_image = db.Column(db.String(length=100), unique=False, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(length=100), unique=False, nullable=False)
    type = db.Column(db.String(length=100), nullable=False)
    Badges_id = db.Column(db.Integer, db.ForeignKey('badges.id'))
    Achievements_id = db.Column(db.Integer, db.ForeignKey('achievements.id'))
    
    children = db.relationship('Progress_Association', back_populates="lessons")
    
class Achievements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(length=255), nullable=False)
    children = db.relationship('Children_Achievements_Association', back_populates="achievements")
    lessons = db.relationship('Lessons', backref="achievements", uselist=False)


class Badges(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(length=100), nullable=False)
    children = db.relationship('Children_Badges_Association', back_populates="badges")
    lessons = db.relationship('Lessons', backref="badges", uselist=False) ##one to one 


