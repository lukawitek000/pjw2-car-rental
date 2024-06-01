from functools import wraps

from flask import Blueprint, request, jsonify
from flask_login import login_user, current_user, LoginManager, logout_user, login_required

from authentication.application.authentication_service import AuthenticationService
from authentication.domain.role import Role
from authentication.domain.user import User
from di import provide_user_repository

auth = Blueprint('auth', __name__)
login_manager = LoginManager()


def set_up_auth(app):
    app.secret_key = "project for passing the course"
    app.register_blueprint(auth)
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    user_repository = provide_user_repository()
    return user_repository.find_by_username(user_id)


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
        login_user(user)
        return jsonify(username=user.username, role=user.role), 200
    except Exception as e:
        return jsonify(message=str(e)), 400


@auth.route('/logout', methods=['POST'])
@login_required
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