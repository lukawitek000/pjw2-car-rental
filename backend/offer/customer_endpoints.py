import json
from datetime import datetime

from flask import Blueprint, jsonify, request

from authentication.auth_decorators import customer_role_required
from offer.application.offer_service import OfferService
from offer.domain.offer_filter_options import OfferFilterOptions
from offer.domain.offer_sort_options import OfferSortOptions
from offer.json_converter import offer_to_dict

customer_endpoints = Blueprint('customer_endpoints', __name__)


def set_up_customer_endpoints(app):
    app.register_blueprint(customer_endpoints)


@customer_endpoints.route("/get_all_offers", methods=['GET'])
@customer_role_required
def get_offers(current_user, offer_service: OfferService):
    start_date_time = request.args.get('start_date_time', "2023-01-01T00:00:00")
    end_date_time = request.args.get('end_date_time', "2023-03-31T00:00:00")
    pickup_location = request.args.get('pickup_location')
    return_location = request.args.get('return_location')
    sort_by_price = request.args.get('sort_by_price')

    start_date_time = datetime.strptime(start_date_time, '%Y-%m-%dT%H:%M:%S') if start_date_time else None
    end_date_time = datetime.strptime(end_date_time, '%Y-%m-%dT%H:%M:%S') if end_date_time else None

    filter_options = OfferFilterOptions(start_date_time=start_date_time, end_date_time=end_date_time,
                                        pickup_location=pickup_location, return_location=return_location)
    sort_options = OfferSortOptions(sort_by_price=sort_by_price)

    offers = offer_service.get_all_offers(filter_options, sort_options)
    offers_dict = [offer_to_dict(offer) for offer in offers]
    return jsonify({"offers": offers_dict}), 200
