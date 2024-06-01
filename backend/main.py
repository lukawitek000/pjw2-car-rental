from flask import Flask
from authentication.auth import set_up_auth
from di import init_di
from database import set_up_database
from offer.owner_operations import set_up_owner_operations

app = Flask(__name__)

if __name__ == '__main__':  # Running the flask app
    set_up_database()
    set_up_owner_operations(app)
    set_up_auth(app)
    init_di(app)
    app.run(host='127.0.0.1', port=5000, debug=True)
