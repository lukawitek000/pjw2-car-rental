from injector import inject
from reservation.domain.reservation import Reservation
from offer.domain.offer import Offer
from offer.domain.invalid_offer_error import InvalidOfferError
from reservation.infrastructure.sqlite_reservation_repository import SqliteReservationRepository


class ReservationService:
    def __init__(self, reservation_repository: SqliteReservationRepository, offer_repository, user_repository):
        self.reservation_repository = reservation_repository,
        self.offer_repository = offer_repository,
        self.user_repository = user_repository

    def make_reservation(self, reservation_details, user_username):
        # offer = self.offer_repository.get_offer(reservation_details['offer_id'])
        # if not offer:
        #     raise ValueError("Offer does not exist")
        #
        # existing_reservations = self.offer_repository.get_reservations_by_offer_id(reservation_details['offer_id'])
        # for existing in existing_reservations:
        #     if reservation_details['start_date_time'] <= existing.end_date_time and reservation_details['end_date_time'] >= existing.start_date_time:
        #         raise InvalidOfferError("The reservation overlaps with an existing reservation")
        reservation = Reservation(
            user_id=user_username,
            offer_id=reservation_details['offer_id'],
            start_date_time=reservation_details['start_date_time'],
            end_date_time=reservation_details['end_date_time']
        )
        reservation.reservation_id = self.reservation_repository[0].create_reservation(reservation)
        return reservation.reservation_id

    def get_reservations_by_user(self, user_id):
        reservations = self.reservation_repository[0].get_reservations_by_user(user_id)
        for reservation in reservations:
            offer = self.offer_repository[0].get_offer(reservation.offer_id)
            reservation.car = offer.car
        return reservations

    def cancel_reservation(self, reservation_id):
        return self.reservation_repository[0].delete_reservation(reservation_id)
