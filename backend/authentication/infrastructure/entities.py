from peewee import *
from flask_login import UserMixin

from authentication.domain.role import Role
from database import BaseModel


class User(UserMixin, BaseModel):
    username = CharField(unique=True, primary_key=True)
    email = CharField(unique=True)
    password_hash = CharField()
    role = CharField()

    @property
    def role_enum(self):
        return Role(self.role)

    @role_enum.setter
    def role_enum(self, role):
        self.role = role.value

    def get_id(self):
        return self.username
