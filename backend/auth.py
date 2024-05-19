from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from infrastructure.db import db
from application.authentication_service import AuthenticationService
from domain.role import Role
from infrastructure.sqlite_user_repository import SqliteUserRepository
from infrastructure.entities import User

auth = Blueprint('auth', __name__)

db.create_tables([User], safe=True)
user_repository = SqliteUserRepository()
auth_service = AuthenticationService(user_repository)

@auth.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    new_user = auth_service.signup(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        role=Role(data['role'])
    )
    if new_user is None:
        return jsonify(message="This username or email is already used."), 400

    return jsonify(id=new_user.id, username=new_user.username, role=new_user.role), 201


@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = auth_service.login(username=data['username'], password=data['password'])
    if user is None:
        return jsonify(message="Invalid username or password."), 401
    return jsonify(id=user.id, username=user.username, role=user.role), 200