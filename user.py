import squlite3
from flask_restful import Resource

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password


class UserRegister(Resource):
    def post(self):
        pass