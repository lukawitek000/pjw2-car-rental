from datetime import datetime
from flask import Blueprint, jsonify, request

from authentication.auth_decorators import login_required
from reservation.application.reservation_service import ReservationService
from offer.domain.invalid_offer_error import InvalidOfferError

reservation_endpoints = Blueprint('reservation_endpoints', __name__)


def set_up_reservation_endpoints(app):
    app.register_blueprint(reservation_endpoints)


@reservation_endpoints.route("/make_reservation", methods=['POST'])
@login_required
def make_reservation(current_user, reservation_service: ReservationService):
    try:
        reservation_details = request.get_json()
        reservation_details['start_date_time'] = datetime.strptime(reservation_details['start_date_time'],
                                                                   '%Y-%m-%dT%H:%M:%S')
        reservation_details['end_date_time'] = datetime.strptime(reservation_details['end_date_time'],
                                                                 '%Y-%m-%dT%H:%M:%S')

        reservation_id = reservation_service.make_reservation(reservation_details, current_user.id)
        return jsonify({"message": "Reservation made successfully", "reservation_id": reservation_id}), 201
    except PermissionError as e:
        return jsonify({"message": str(e)}), 403
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
    except InvalidOfferError as e:
        return jsonify({"message": str(e)}), 400


@reservation_endpoints.route("/my_reservations", methods=['GET'])
@login_required
def get_my_reservations(current_user, reservation_service: ReservationService):
    reservations = reservation_service.get_reservations_by_user(current_user.id)
    reservations_dict = [reservation_to_dict(reservation) for reservation in reservations]
    return jsonify({"reservations": reservations_dict}), 200


@reservation_endpoints.route("/cancel_reservation/<int:reservation_id>", methods=['DELETE'])
@login_required
def cancel_reservation(current_user, reservation_service: ReservationService, reservation_id):
    try:
        reservation_service.cancel_reservation(reservation_id)
        return jsonify({"message": "Reservation cancelled successfully"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
