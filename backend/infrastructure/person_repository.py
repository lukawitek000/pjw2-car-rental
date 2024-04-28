from infrastructure.db import db
from infrastructure.person import Person


class PersonRepository:
    def save(self, name, birthday):
        person = Person(name=name, birthday=birthday)
        person.save()

    def get_all(self):
        return [person for person in Person.select().dicts()]