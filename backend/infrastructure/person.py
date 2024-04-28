from peewee import *
from infrastructure.db import db

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db