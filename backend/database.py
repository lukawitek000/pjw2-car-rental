from peewee import SqliteDatabase


database = SqliteDatabase('database/my_app.db')


def set_up_database():
    from authentication.infrastructure.entities import User
    database.create_tables([User], safe=True)
    if database.is_closed():
        database.connect()
