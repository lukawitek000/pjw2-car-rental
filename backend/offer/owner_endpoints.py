from datetime import datetime

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user

from authentication.auth_endpoints import car_owner_role_required
from offer.application.offer_service import OfferService
from offer.domain.invalid_offer_error import InvalidOfferError
from offer.json_converter import offer_to_dict

owner_operations = Blueprint('owner_operations', __name__)


def set_up_owner_endpoints(app):
    app.register_blueprint(owner_operations)


@owner_operations.route("/add_car", methods=['POST'])
@login_required
@car_owner_role_required
def add_car(offer_service: OfferService):
    car_details = request.get_json()
    owner_username = current_user.username
    car_id = offer_service.add_car(car_details, owner_username)
    return jsonify({"message": "Car added successfully", "car_id": car_id}), 201


@owner_operations.route("/add_offer", methods=['POST'])
@login_required
@car_owner_role_required
def add_offer(offer_service: OfferService):
    try:
        offer_details = request.get_json()
        owner_username = current_user.username
        offer_details['start_date_time'] = datetime.strptime(offer_details['start_date_time'], '%Y-%m-%dT%H:%M:%S')
        offer_details['end_date_time'] = datetime.strptime(offer_details['end_date_time'], '%Y-%m-%dT%H:%M:%S')
        offer_id = offer_service.add_offer(offer_details, owner_username)
        return jsonify({"message": "Offer added successfully", "offer_id": offer_id}), 201
    except PermissionError as e:
        return jsonify({"message": str(e)}), 403
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
    except InvalidOfferError as e:
        return jsonify({"message": str(e)}), 400


@owner_operations.route("/get_all_offers_for_car/<int:param>", methods=['GET'])
@login_required
@car_owner_role_required
def get_all_offers_for_car(offer_service: OfferService, param):
    offers = offer_service.get_all_offers_for_car(param)
    offers_dict = [offer_to_dict(offer) for offer in offers]
    return jsonify({"offers": offers_dict}), 200
