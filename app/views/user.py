from flask import request
from flask_restx import Resource, Namespace

from container import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def post(self):
        data = request.json
        user = user_service.create_user(data)
        return user, 201


