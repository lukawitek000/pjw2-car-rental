from peewee import SqliteDatabase, Model


database = SqliteDatabase('database/my_app.db')


def set_up_database():
    from authentication.infrastructure.user_entity import UserEntity
    from offer.infrastructure.car_entity import CarEntity
    from offer.infrastructure.offer_entity import OfferEntity
    database.create_tables([UserEntity, OfferEntity, CarEntity], safe=True)
    if database.is_closed():
        database.connect()


class BaseModel(Model):
    class Meta:
        database = database
