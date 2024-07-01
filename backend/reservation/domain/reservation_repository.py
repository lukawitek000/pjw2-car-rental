from abc import ABC, abstractmethod

from reservation.domain.reservation import Reservation


class ReservationRepository(ABC):
    @abstractmethod
    def create_reservation(self, reservation: Reservation) -> int:
        pass

    @abstractmethod
    def get_reservations_by_offer_id(self, offer_id: int) -> list:
        pass

    @abstractmethod
    def get_reservations_by_user_id(self, user_id: int) -> list:
        pass

    @abstractmethod
    def delete_reservation(self, reservation_id: int):
        pass