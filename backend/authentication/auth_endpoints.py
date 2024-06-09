from flask import Blueprint, request, jsonify, g

from authentication.application.authentication_service import AuthenticationService, UserNotFoundException
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
        (user, token) = auth_service.login(username=data['username'], password=data['password'])
    except UserNotFoundException:
        return jsonify(message="Invalid username."), 401

    return jsonify(username=user.username, role=user.role, token=token), 200
