from flask_injector import FlaskInjector
from injector import Binder

from authentication.domain.user_repository import UserRepository
from authentication.infrastructure.sqlite_user_repository import SqliteUserRepository


def configure(binder: Binder):
    binder.bind(
        UserRepository,
        to=SqliteUserRepository()
    )


def init_di(app):
    FlaskInjector(app=app, modules=[configure])
