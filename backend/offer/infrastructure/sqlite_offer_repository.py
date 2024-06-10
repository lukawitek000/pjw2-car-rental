from offer.domain.car import Car
from offer.domain.offer_repository import OfferRepository
from offer.domain.offer_sort_options import SortByPrice
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

    def get_all_offers(self, filter_options, sort_options) -> list:
        query = OfferEntity.select()

        if filter_options.start_date_time is not None:
            query = query.where(OfferEntity.start_date_time <= filter_options.start_date_time)
        if filter_options.end_date_time is not None:
            query = query.where(OfferEntity.end_date_time >= filter_options.end_date_time)

        if sort_options.sort_by_price is not None:
            if sort_options.sort_by_price == SortByPrice.FROM_LOWEST:
                query = query.order_by(OfferEntity.price_per_day.asc())
            else:
                query = query.order_by(OfferEntity.price_per_day.desc())
        return [offer.to_domain_model() for offer in query]

    def get_offers_by_car_id(self, car_id) -> list:
        return [offer.to_domain_model() for offer in OfferEntity.select().where(OfferEntity.car == car_id)]

    def get_cars_by_owner_id(self, owner_id) -> list:
        return [car.to_domain_model() for car in CarEntity.select().where(CarEntity.owner == owner_id)]

    def delete_offers_by_car_id(self, car_id):
        query = OfferEntity.delete().where(OfferEntity.car == car_id)
        query.execute()
        self.delete_car_by_id(car_id)

    def delete_car_by_id(self, car_id):
        query = CarEntity.delete().where(CarEntity.car_id == car_id)
        query.execute()


    def get_offers_by_owner_id(self, owner_id) -> list:
        return [offer.to_domain_model() for offer in OfferEntity.select().where(OfferEntity.offerer_id == owner_id)]
