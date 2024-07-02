from abc import ABC, abstractmethod

from offer.domain.car import Car
from offer.domain.offer import Offer


class OfferRepository(ABC):
    @abstractmethod
    def create_offer(self, offer) -> int:
        pass

    @abstractmethod
    def create_car(self, car, owner) -> int:
        pass

    @abstractmethod
    def get_car(self, car_id) -> Car:
        pass

    @abstractmethod
    def get_all_offers(self, filter_options, sort_options) -> list:
        pass

    @abstractmethod
    def get_offers_by_car_id(self, car_id) -> list:
        pass

    @abstractmethod
    def get_cars_by_owner_id(self, owner_id) -> list:
        pass

    @abstractmethod
    def delete_offers_by_car_id(self, car_id):
        pass

    @abstractmethod
    def get_offers_by_owner_id(self, owner_id) -> list:
        pass

    @abstractmethod
    def get_offer_by_id(self, offer_id) -> Offer:
        pass
