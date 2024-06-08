import os
from functools import wraps

import jwt
from flask import request, jsonify, g
from injector import inject

from authentication.application.authentication_service import AuthenticationService
from authentication.infrastructure.user_entity import UserEntity

@inject
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_service = g.get('auth_service')
        token = request.headers.get('Authorization')
        token = token.split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401

        try:
            current_user = auth_service.find_user_by_jwt_token(token)
            # decoding the payload to fetch the stored details
            # data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
            # current_user = UserEntity.query.filter_by(username=data['username']).first()
        except Exception as e:
            print(e)
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return f(current_user, *args, **kwargs)

    return decorated

# def car_owner_role_required(view_func):
#     @wraps(view_func)
#     def decorated_view(**kwargs):
#         if current_user.role != Role.CAR_OWNER.value:
#             return jsonify(message="Access denied."), 403
#         return view_func(**kwargs)
#     return decorated_view
#
#
# def customer_role_required(view_func):
#     @wraps(view_func)
#     def decorated_view(**kwargs):
#         if current_user.role != Role.CUSTOMER.value:
#             return jsonify(message="Access denied."), 403
#         return view_func(**kwargs)
#     return decorated_view