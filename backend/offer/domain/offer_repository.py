from abc import ABC, abstractmethod

from offer.domain.car import Car


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
