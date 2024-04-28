from flask import Flask, jsonify
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
