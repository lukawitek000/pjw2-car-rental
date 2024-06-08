from datetime import datetime

from peewee import *

from authentication.infrastructure.user_entity import UserEntity
from database import BaseModel
from offer.domain.offer import Offer
from offer.infrastructure.car_entity import CarEntity


class OfferEntity(BaseModel):
    offer_id = AutoField()
    car = ForeignKeyField(CarEntity, backref='offers', to_field='car_id')
    offerer = ForeignKeyField(UserEntity, backref='offers', to_field='username')
    price_per_day = DecimalField(decimal_places=2)
    extra_features = TextField()
    start_date_time = DateTimeField()
    end_date_time = DateTimeField()
    pickup = CharField()
    return_location = CharField()

    @staticmethod
    def from_domain_model(offer):
        return OfferEntity(
            car=CarEntity.get(CarEntity.car_id == offer.car.car_id),
            offerer=UserEntity.get(UserEntity.username == offer.user_id),
            price_per_day=offer.price_per_day,
            extra_features=offer.extra_features,
            start_date_time=offer.start_date_time,
            end_date_time=offer.end_date_time,
            pickup=offer.pickup_location,
            return_location=offer.return_location
        )

    def to_domain_model(self):
        return Offer(
            offer_id=self.offer_id,
            car=self.car.to_domain_model(),
            user_id=self.offerer_id,
            price_per_day=self.price_per_day,
            extra_features=self.extra_features,
            start_date_time=self.start_date_time,
            end_date_time=self.end_date_time,
            pickup_location=self.pickup,
            return_location=self.return_location
        )
