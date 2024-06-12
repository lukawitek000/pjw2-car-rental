from abc import ABC, abstractmethod

from reservation.domain.reservation import Reservation

class ReservationRepository(ABC):
    @abstractmethod
    def create_reservation(self, offer) -> int:
        pass