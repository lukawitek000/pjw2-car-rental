from injector import inject

from offer.domain.car import Car
from offer.domain.offer import Offer
from offer.domain.offer_filter_by_location import OfferFilterByLocation


class OfferService:
    def __init__(self, offer_repository, user_repository):
        self.offer_repository = offer_repository
        self.user_repository = user_repository

    def add_offer(self, offer_details, owner_username):
        car_id = offer_details.pop('car_id')
        car = self.offer_repository.get_car(car_id)
        if car is None:
            raise ValueError(f"Car with ID {car_id} does not exist")
        if car.owner_id != owner_username:
            raise PermissionError("You are not the owner of this car")

        existing_offers = self.offer_repository.get_offers_by_car_id(car_id)

        offer = Offer(user_id=owner_username, car=car, **offer_details)

        offer.validate(existing_offers)

        offer.offer_id = self.offer_repository.create_offer(offer)
        return offer.offer_id

    def add_car(self, car_details, owner_username):
        car = Car(owner_id=owner_username, **car_details)
        owner = self.user_repository.find_by_username(owner_username)
        car.car_id = self.offer_repository.create_car(car, owner)
        return car.car_id

    def get_all_offers(self, filter_options, sort_options):
        all_offers = self.offer_repository.get_all_offers(filter_options, sort_options)
        offer_filter = OfferFilterByLocation(all_offers, filter_options.pickup_location, filter_options.return_location,
                                             filter_options.radius_km)
        return offer_filter.filter_offers()

    def get_all_offers_for_car(self, car_id):
        return self.offer_repository.get_offers_by_car_id(car_id)

    def get_all_owned_cars(self, owner_username):
        return self.offer_repository.get_cars_by_owner_id(owner_username)
