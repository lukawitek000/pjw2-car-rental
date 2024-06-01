import json

from flask import Blueprint, jsonify
from flask_login import login_required

from authentication.auth import customer_role_required
from offer.application.offer_service import OfferService
from offer.json_converter import offer_to_dict

customer_endpoints = Blueprint('customer_endpoints', __name__)


def set_up_customer_endpoints(app):
    app.register_blueprint(customer_endpoints)


@customer_endpoints.route("/get_all_offers", methods=['GET'])
def get_offers(offer_service: OfferService):
    offers = offer_service.get_all_offers()
    offers_dict = [offer_to_dict(offer) for offer in offers]
    return jsonify(offers_dict), 200
