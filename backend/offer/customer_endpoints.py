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


@customer_endpoints.route("/get_all_offers", methods=['GET'], defaults={'start_date_time': "2023-01-01T00:00:00", 'end_date_time': "2023-03-31T00:00:00", 'pickup_location': None, 'return_location': None, 'sort_by_price': None})
@customer_endpoints.route("/get_all_offers/<string:start_date_time>", methods=['GET'], defaults={'end_date_time': "2023-03-31T00:00:00", 'pickup_location': None, 'return_location': None, 'sort_by_price': None})
@customer_endpoints.route("/get_all_offers/<string:start_date_time>/<string:end_date_time>", methods=['GET'], defaults={'pickup_location': None, 'return_location': None, 'sort_by_price': None})
@customer_endpoints.route("/get_all_offers/<string:start_date_time>/<string:end_date_time>/<string:pickup_location>", methods=['GET'], defaults={'return_location': None, 'sort_by_price': None})
@customer_endpoints.route("/get_all_offers/<string:start_date_time>/<string:end_date_time>/<string:pickup_location>/<string:return_location>", methods=['GET'], defaults={'sort_by_price': None})
@customer_endpoints.route("/get_all_offers/<string:start_date_time>/<string:end_date_time>/<string:pickup_location>/<string:return_location>/<string:sort_by_price>", methods=['GET'])
def get_offers(offer_service: OfferService, start_date_time="2023-01-01T00:00:00", end_date_time="2023-03-31T00:00:00", pickup_location=None, return_location=None, sort_by_price=None):
    start_date_time = datetime.strptime(start_date_time, '%Y-%m-%dT%H:%M:%S')
    end_date_time = datetime.strptime(end_date_time, '%Y-%m-%dT%H:%M:%S')

    filter_options = OfferFilterOptions(start_date_time=start_date_time, end_date_time=end_date_time,
                                        pickup_location=pickup_location, return_location=return_location)
    sort_options = OfferSortOptions(sort_by_price=sort_by_price)

    offers = offer_service.get_all_offers(filter_options, sort_options)
    offers_dict = [offer_to_dict(offer) for offer in offers]
    return jsonify({"offers": offers_dict}), 200
