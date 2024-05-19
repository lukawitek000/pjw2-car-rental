from peewee import *
from flask_login import UserMixin

from domain.role import Role
from infrastructure.database import database


class BaseModel(Model):
    class Meta:
        database = database


class User(UserMixin, BaseModel):
    id = AutoField()
    username = CharField(unique=True)
    email = CharField(unique=True)
    password_hash = CharField()
    role = CharField()

    @property
    def role_enum(self):
        return Role(self.role)

    @role_enum.setter
    def role_enum(self, role):
        self.role = role.value
