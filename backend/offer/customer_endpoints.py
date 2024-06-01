from flask import Blueprint, jsonify
from flask_login import login_required

from authentication.auth import customer_role_required
from offer.application.offer_service import OfferService

customer_endpoints = Blueprint('customer_endpoints', __name__)


def set_up_customer_endpoints(app):
    app.register_blueprint(customer_endpoints)


@customer_endpoints.route("/get_all_offers", methods=['GET'])
@login_required
@customer_role_required
def get_offers(offer_service: OfferService):
    offers = offer_service.get_all_offers()
    return jsonify(offers), 200
