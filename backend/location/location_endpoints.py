from flask import Blueprint, request, jsonify

from authentication.auth_decorators import login_required
from location.application.location_service import LocationService

location_endpoints = Blueprint('location_endpoints', __name__)


def set_up_location_endpoints(app):
    app.register_blueprint(location_endpoints)


@location_endpoints.route("/autocomplete", methods=['GET'])
@login_required
def autocomplete(current_user, location_service: LocationService):
    query = request.args.get('query')
    if not query:
        return jsonify({"suggestions": []}), 200
    try:
        suggestions = location_service.find_auto_complete(query)
    except:
        return jsonify({"suggestions": []}), 200
    return jsonify({"suggestions": suggestions}), 200