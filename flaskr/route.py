from flask import request
from flask_restful import Resource
from flaskr.__init__ import api


user = {}

class Signin(Resource):
    def get(self, user_id):
        return {user_id: user[user_id]}
    def put(self, user_id):
        user[user_id] = request.form['data']
        return {user_id : user[user_id]}
        
api.add_resource(Signin, '/<string:user_id>')