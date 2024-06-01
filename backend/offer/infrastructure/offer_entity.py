from peewee import *

from database import BaseModel


class OfferEntity(BaseModel):
    offer_id = AutoField()
    car_id = IntegerField()
    user_id = IntegerField()
    price_per_day = DecimalField(decimal_places=2)
    extra_features = TextField()
    start_date_time = DateTimeField()
    end_date_time = DateTimeField()
    pickup = CharField()
    return_location = CharField()

    @staticmethod
    def from_domain_model(offer):
        return OfferEntity(
            car_id=offer.car.car_id,
            user_id=offer.user_id,
            price_per_day=offer.price_per_day,
            extra_features=offer.extra_features,
            start_date_time=offer.start_date_time,
            end_date_time=offer.end_date_time,
            pickup=offer.pickup_location,
            return_location=offer.return_location
        )
