from functools import wraps

from flask import request, jsonify, g
from injector import inject

from authentication.domain.role import Role


class AuthenticationException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


def retrieve_current_user():
    auth_service = g.get('auth_service')
    token = request.headers.get('Authorization')

    if not token:
        raise AuthenticationException('Token is missing', 401)

    token = token.split(" ")[1]

    try:
        current_user = auth_service.find_user_by_jwt_token(token)
    except:
        raise AuthenticationException('Token is invalid', 401)
    return current_user


@inject
def login_required(fun):
    @wraps(fun)
    def decorated(*args, **kwargs):
        try:
            current_user = retrieve_current_user()
        except AuthenticationException as e:
            return jsonify(message=e.message), e.code
        return fun(current_user, *args, **kwargs)

    return decorated


def car_owner_role_required(fun):
    @wraps(fun)
    def decorated(*args, **kwargs):
        try:
            current_user = retrieve_current_user()
        except AuthenticationException as e:
            return jsonify(message=e.message), e.code
        if current_user.role != Role.CAR_OWNER.value:
            return jsonify(message="Access denied."), 403
        return fun(current_user, *args, **kwargs)

    return decorated


def customer_role_required(fun):
    @wraps(fun)
    def decorated(*args, **kwargs):
        current_user = retrieve_current_user()
        if current_user.role != Role.CUSTOMER.value:
            return jsonify(message="Access denied."), 403
        return fun(current_user, *args, **kwargs)

    return decorated
