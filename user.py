import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def find_by_username(self, username):
        connection = sqlite3.connect('data.db')
        sursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = curson.execute(query, (username,))
				row = result.fetchone()
				if row:
            user = User(rpw[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field cannot be blank")
    parser.add_argument('password', type=str, required=True, help="This field cnanot be blank")
    
    def post(self):
        data = UserRegister.parser.parse_args()

        connection = squlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201