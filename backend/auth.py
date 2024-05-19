from functools import wraps

from flask import Blueprint, request, jsonify
from flask_login import login_user, current_user, LoginManager, logout_user
from application.authentication_service import AuthenticationService
from domain.role import Role
from infrastructure.sqlite_user_repository import SqliteUserRepository
from infrastructure.entities import User

auth = Blueprint('auth', __name__)
login_manager = LoginManager()


user_repository = SqliteUserRepository()
auth_service = AuthenticationService(user_repository)


def set_up_auth(app):
    app.secret_key = "project for passing the course"
    app.register_blueprint(auth)
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return user_repository.find_by_id(user_id)


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
    login_user(user)
    return jsonify(id=user.id, username=user.username, role=user.role), 200


@auth.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify(message="Logged out successfully."), 200


def car_owner_role_required(view_func):
    @wraps(view_func)
    def decorated_view(**kwargs):
        if current_user.role != Role.CAR_OWNER.value:
            return jsonify(message="Access denied."), 403
        return view_func(**kwargs)
    return decorated_view


def customer_role_required(view_func):
    @wraps(view_func)
    def decorated_view(**kwargs):
        if current_user.role != Role.CUSTOMER.value:
            return jsonify(message="Access denied."), 403
        return view_func(**kwargs)
    return decorated_view