from flask_injector import FlaskInjector
from injector import Binder

from domain.user_repository import UserRepository
from infrastructure.sqlite_user_repository import SqliteUserRepository


def configure(binder: Binder):
    binder.bind(
        UserRepository,
        to=SqliteUserRepository()
    )


def init_di(app):
    FlaskInjector(app=app, modules=[configure])
