from offer.domain.car import Car
from offer.domain.offer_repository import OfferRepository
from offer.infrastructure.car_entity import CarEntity
from offer.infrastructure.offer_entity import OfferEntity


class SqliteOfferRepository(OfferRepository):
    def create_offer(self, offer) -> int:
        offer_entity = OfferEntity.from_domain_model(offer)
        offer_entity.save()
        return offer_entity.offer_id

    def create_car(self, car, owner) -> int:
        car_entity = CarEntity.from_domain_model(car, owner)
        car_entity.save()
        return car_entity.car_id

    def get_car(self, car_id) -> Car:
        car_entity = CarEntity.get_or_none(CarEntity.car_id == car_id)
        if car_entity is None:
            return None
        return car_entity.to_domain_model()
