from peewee import SqliteDatabase

from infrastructure.entities import User

database = SqliteDatabase('database/my_app.db')


def set_up_database():
    database.create_tables([User], safe=True)
    database.connect()
