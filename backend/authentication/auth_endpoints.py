import os
from datetime import datetime, timedelta

import jwt
from flask import Blueprint, request, jsonify, g
from injector import inject

from authentication.application.authentication_service import AuthenticationService
from authentication.auth_decorators import login_required
from authentication.domain.role import Role
from authentication.domain.user import User

auth = Blueprint('auth', __name__)


def set_up_auth(app):
    app.secret_key = "project for passing the course"
    app.register_blueprint(auth)





@auth.route('/signup', methods=['POST'])
def signup(auth_service: AuthenticationService):
    data = request.get_json()
    password = data.pop('password')
    role = data.pop('role')
    user = User(**data, role=Role(role))
    new_user = auth_service.signup(user, password)
    if new_user is None:
        return jsonify(message="This username or email is already used."), 400

    return jsonify(username=new_user.username, role=new_user.role), 201


@auth.route('/login', methods=['POST'])
def login(auth_service: AuthenticationService):
    data = request.get_json()
    try:
        user = auth_service.login(username=data['username'], password=data['password'])
        if user is None:
            return jsonify(message="Invalid password."), 401
        token = jwt.encode({
            'username': user.username,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, os.getenv('SECRET_KEY'), algorithm="HS256")
        return jsonify(username=user.username, role=user.role, token=token), 200
    except Exception as e:
        return jsonify(message=str(e)), 404


@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    # logout_user()
    return jsonify(message="Logged out successfully."), 200

