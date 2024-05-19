from flask import Flask, jsonify
from flask_login import login_required

from auth import set_up_auth, car_owner_role_required, customer_role_required
from infrastructure.person_repository import PersonRepository
from infrastructure.person import Person
from infrastructure.db import db


app = Flask(__name__)

db.connect()
db.create_tables([Person], safe=True)
repo = PersonRepository()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/save/<name>/<birthday>", methods=['POST'])
def save_person(name, birthday):
    repo.save(name, birthday)
    return "<p>Person saved!</p>"

@app.route("/get_all")
def get_all():
    people = repo.get_all()
    return jsonify(people)


@app.route("/add_car", methods=['POST'])
@login_required
@car_owner_role_required
def add_car():
    return "<p>Car added!</p>"

@app.route("/rent_car", methods=['POST'])
@login_required
@customer_role_required
def rent_car():
    return "<p>Car rented!</p>"

@app.route("/get_all_offers")
@login_required
def get_all_offers():
    return "<p>All offers!</p>"


if __name__ == '__main__':  # Running the flask app
    set_up_auth(app)
    app.run(host='127.0.0.1', port=5000, debug=True)