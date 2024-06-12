from reservation.domain.reservation import Reservation
from offer.domain.invalid_offer_error import InvalidOfferError

class ReservationService:
    def __init__(self, reservation_repository, offer_repository, user_repository):
        self.reservation_repository = reservation_repository,
        self.offer_repository = offer_repository,
        self.user_repository = user_repository

    def make_reservation(self, reservation_details, user_id):
        offer = self.offer_repository.get_offer(reservation_details['offer_id'])
        if not offer:
            raise ValueError("Offer does not exist")

        existing_reservations = self.offer_repository.get_reservations_by_offer_id(reservation_details['offer_id'])
        for existing in existing_reservations:
            if reservation_details['start_date_time'] <= existing.end_date_time and reservation_details['end_date_time'] >= existing.start_date_time:
                raise InvalidOfferError("The reservation overlaps with an existing reservation")

        reservation = Reservation(
            user_id=user_id,
            offer_id=reservation_details['offer_id'],
            start_date_time=reservation_details['start_date_time'],
            end_date_time=reservation_details['end_date_time']
        )
        return self.offer_repository.create_reservation(reservation)

    def get_reservations_by_user(self, user_id):
        return self.offer_repository.get_reservations_by_user_id(user_id)

    def cancel_reservation(self, reservation_id):
        self.offer_repository.delete_reservation(reservation_id)
