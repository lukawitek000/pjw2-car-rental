from flask_login import login_required
from auth import *

draft = Blueprint('draft', __name__)


def set_up_draft_endpoints(app):
    app.register_blueprint(draft)


@draft.route("/add_car", methods=['POST'])
@login_required
@car_owner_role_required
def add_car():
    return "<p>Car added!</p>"


@draft.route("/rent_car", methods=['POST'])
@login_required
@customer_role_required
def rent_car():
    return "<p>Car rented!</p>"


@draft.route("/get_all_offers")
@login_required
def get_all_offers():
    return "<p>All offers!</p>"