from flask import request
from flask_restx import Namespace, Resource

from container import auth_service

auth_ns = Namespace("auth")


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get("username", None)
        password = req_json("password", None)
        if None in [username, password]:
            return "", 400
        tokens = auth_service.generate_tokens(username, password)
        return tokens

    def put(self):
        data = request.json
        token = data.get("refresh_token")
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201
