from peewee import *

from offer.infrastructure.offer_entity import OfferEntity
from authentication.infrastructure.user_entity import UserEntity
from reservation.domain.reservation import Reservation


class ReservationEntity(Model):
    reservation_id = AutoField()
    user_id = ForeignKeyField(UserEntity, backref='reservations', to_field='username')
    offer = ForeignKeyField(OfferEntity, backref='reservations', to_field='offer_id')
    start_date_time = DateTimeField()
    end_date_time = DateTimeField()

    @classmethod
    def from_domain_model(reservation):
        return ReservationEntity(
            user=UserEntity.get(UserEntity.username == reservation.user_id),
            offer=OfferEntity.get(OfferEntity.offer_id == reservation.offer.offer_id),
            start_date_time=reservation.start_date_time,
            end_date_time=reservation.end_date_time
        )

    def to_domain_model(self):
        return Reservation(
            user_id=self.user_id,
            offer_id=self.offer.to_domain_model(),
            start_date_time=self.start_date_time,
            end_date_time=self.end_date_time,
            reservation_id=self.reservation_id
        )
