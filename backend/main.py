from flask import Flask
from auth import set_up_auth, car_owner_role_required, customer_role_required
from di import init_di
from draft_endpoints import set_up_draft_endpoints
from infrastructure.database import set_up_database

app = Flask(__name__)


if __name__ == '__main__':  # Running the flask app
    set_up_database()
    init_di(app)
    set_up_auth(app)
    set_up_draft_endpoints(app)
    app.run(host='127.0.0.1', port=5000, debug=True)