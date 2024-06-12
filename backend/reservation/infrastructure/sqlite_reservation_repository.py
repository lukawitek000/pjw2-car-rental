from reservation.domain.reservation_repository import ReservationRepository
from reservation.infrastructure.reservation_entity import ReservationEntity

class SqliteReservationRepository(ReservationRepository):
    def create_reservation(self, reservation) -> int:
        reservation_entity = ReservationEntity.from_domain_model(reservation)
        reservation_entity.save()
        return reservation_entity.reservation_id