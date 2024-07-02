from datetime import datetime

from flask import Blueprint, request, jsonify

from authentication.auth_decorators import car_owner_role_required
from location.application.location_service import LocationService
from location.domain.geocoding_exceptions import NoResultsFoundForAddressException, GeocodingRequestFailed
from offer.application.offer_service import OfferService
from offer.domain.invalid_offer_error import InvalidOfferError
from offer.json_converter import offer_to_dict, car_to_dict

owner_operations = Blueprint('owner_operations', __name__)


def set_up_owner_endpoints(app):
    app.register_blueprint(owner_operations)


@owner_operations.route("/add_car", methods=['POST'])
@car_owner_role_required
def add_car(current_user, offer_service: OfferService):
    car_details = request.get_json()
    owner_username = current_user.username
    car_id = offer_service.add_car(car_details, owner_username)
    return jsonify({"message": "Car added successfully", "car_id": car_id}), 201


@owner_operations.route("/add_offer", methods=['POST'])
@car_owner_role_required
def add_offer(current_user, offer_service: OfferService, location_service: LocationService):
    try:
        offer_details = request.get_json()
        owner_username = current_user.username
        offer_details['start_date_time'] = datetime.strptime(offer_details['start_date_time'], '%Y-%m-%dT%H:%M:%S')
        offer_details['end_date_time'] = datetime.strptime(offer_details['end_date_time'], '%Y-%m-%dT%H:%M:%S')
        try:
            offer_details['pickup_location'] = location_service.find_coordinates_for_address(offer_details['pickup_location'])
        except (NoResultsFoundForAddressException, GeocodingRequestFailed) as e:
            return jsonify({"message": f"Wrong pick up location: {str(e)}"}), 418

        try:
            offer_details['return_location'] = location_service.find_coordinates_for_address(offer_details['return_location'])
        except (NoResultsFoundForAddressException, GeocodingRequestFailed) as e:
            return jsonify({"message": f"Wrong return location: {str(e)}"}), 418
        offer_id = offer_service.add_offer(offer_details, owner_username)
        return jsonify({"message": "Offer added successfully", "offer_id": offer_id}), 201
    except PermissionError as e:
        return jsonify({"message": str(e)}), 403
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
    except InvalidOfferError as e:
        return jsonify({"message": str(e)}), 400


@owner_operations.route("/get_all_offers_for_car/<int:param>", methods=['GET'])
@car_owner_role_required
def get_all_offers_for_car(current_user, offer_service: OfferService, location_service: LocationService, param):
    offers = offer_service.get_all_offers_for_car(param)
    offers_dict = []
    for offer in offers:
        offer_dict = offer_to_dict(offer)
        offer_dict["pickup_location"] = location_service.find_address_for_coordinates(offer.pickup_location)
        offer_dict["return_location"] = location_service.find_address_for_coordinates(offer.return_location)
        offers_dict.append(offer_dict)
    return jsonify({"offers": offers_dict}), 200


@owner_operations.route("/get_all_owned_cars", methods=['GET'])
@car_owner_role_required
def get_all_owned_cars(current_user, offer_service: OfferService):
    cars = offer_service.get_all_owned_cars(current_user.username)
    cars_dict = [car_to_dict(car) for car in cars]
    return jsonify({"cars": cars_dict}), 200


@owner_operations.route("/remove_car/<int:param>", methods=['DELETE'])
@car_owner_role_required
def remove_car_and_related_offers(current_user, offer_service: OfferService, param):
    try:
        offers = offer_service.delete_all_offers_for_car(param)
        return jsonify({"message": "Car and related offers removed successfully"}), 201
    except InvalidOfferError as e:
        return jsonify({"message": str(e)}), 400


@owner_operations.route("/get_all_owned_offers", methods=['GET'])
@car_owner_role_required
def get_all_owned_offers(current_user, offer_service: OfferService, location_service: LocationService):
    offers = offer_service.get_all_owned_offers(current_user.username)
    offers_dict = []
    for offer in offers:
        offer_dict = offer_to_dict(offer)
        offer_dict["pickup_location"] = location_service.find_address_for_coordinates(offer.pickup_location)
        offer_dict["return_location"] = location_service.find_address_for_coordinates(offer.return_location)
        offers_dict.append(offer_dict)
    return jsonify({"offers": offers_dict}), 200