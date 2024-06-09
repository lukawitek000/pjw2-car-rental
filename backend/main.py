import os

from dotenv import load_dotenv
from flask import Flask, g
from flask_cors import CORS
from injector import inject

from authentication.application.authentication_service import AuthenticationService
from authentication.auth_endpoints import set_up_auth
from data.data_endpoints import set_up_data_endpoints
from di import init_di
from database import set_up_database
from location.location_endpoints import set_up_location_endpoints
from offer.customer_endpoints import set_up_customer_endpoints
from offer.owner_endpoints import set_up_owner_endpoints

app = Flask(__name__)
load_dotenv()
CORS(app, resources={r"/*": {"origins": os.getenv("CORS-ORIGIN")}})


@inject
@app.before_request
def before_request(service: AuthenticationService):
    g.auth_service = service


if __name__ == '__main__':  # Running the flask app
    set_up_database()
    set_up_data_endpoints(app)
    set_up_owner_endpoints(app)
    set_up_customer_endpoints(app)
    set_up_auth(app)
    set_up_location_endpoints(app)
    init_di(app)
    app.run(host='127.0.0.1', port=8000, debug=True)
