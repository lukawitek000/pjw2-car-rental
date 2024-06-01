from peewee import *

from authentication.domain.role import Role
from authentication.domain.user import User
from database import BaseModel


class UserEntity(BaseModel):
    username = CharField(primary_key=True, unique=True)
    email = CharField(unique=True)
    password_hash = CharField()
    name = CharField()
    role = CharField()

    @property
    def role_enum(self):
        return Role(self.role)

    @role_enum.setter
    def role_enum(self, role):
        self.role = role.value

    def to_domain_model(self):
        return User(
            username=self.username,
            email=self.email,
            role=self.role_enum,
            name=self.name
        )

    @staticmethod
    def from_domain_model(user, password_hash):
        return UserEntity(
            username=user.username,
            email=user.email,
            name=user.name,
            password_hash=password_hash,
            role=user.role.value
        )
