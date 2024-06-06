import json
from datetime import datetime

from flask import Blueprint, jsonify, request

from offer.application.offer_service import OfferService
from offer.domain.offer_filter_options import OfferFilterOptions
from offer.domain.offer_sort_options import OfferSortOptions
from offer.json_converter import offer_to_dict

customer_endpoints = Blueprint('customer_endpoints', __name__)


def set_up_customer_endpoints(app):
    app.register_blueprint(customer_endpoints)


@customer_endpoints.route("/get_all_offers", methods=['GET'])
def get_offers(offer_service: OfferService):
    params_json = request.get_json() or {}

    default_filter_params = {
        'start_date_time': "2023-01-01T00:00:00",
        'end_date_time': "2023-03-31T00:00:00",
        'pickup_location': None,
        'return_location': None
    }

    default_sort_params = {
        'sort_by_price': None
    }

    filter_params_json = params_json.get('filter', default_filter_params)
    filter_params_json['start_date_time'] = datetime.strptime(filter_params_json['start_date_time'], '%Y-%m-%dT%H:%M:%S')
    filter_params_json['end_date_time'] = datetime.strptime(filter_params_json['end_date_time'], '%Y-%m-%dT%H:%M:%S')

    sort_params_json = params_json.get('sort', default_sort_params)

    filter_options = OfferFilterOptions(**filter_params_json)
    sort_options = OfferSortOptions(**sort_params_json)

    offers = offer_service.get_all_offers(filter_options, sort_options)
    offers_dict = [offer_to_dict(offer) for offer in offers]
    return jsonify({"offers": offers_dict}), 200
