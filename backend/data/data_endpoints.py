from flask import Blueprint, jsonify

from authentication.auth_decorators import login_required
from data.car_data import car_manufacturers

data = Blueprint("data", __name__)


def set_up_data_endpoints(app):
    app.register_blueprint(data)


@data.route("/car_models", methods=['GET'])
@login_required
def get_car_models(current_user):
    car_manufacturers_dict = [manufacturer.to_dict() for manufacturer in car_manufacturers]
    return jsonify({"cars": car_manufacturers_dict}), 200