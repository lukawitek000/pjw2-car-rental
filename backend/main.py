from flask import Flask
from authentication.auth import set_up_auth
from di import init_di
from draft_endpoints import set_up_draft_endpoints
from database import set_up_database

app = Flask(__name__)

if __name__ == '__main__':  # Running the flask app
    set_up_database()
    init_di(app)
    set_up_auth(app)
    set_up_draft_endpoints(app)
    app.run(host='127.0.0.1', port=5000, debug=True)