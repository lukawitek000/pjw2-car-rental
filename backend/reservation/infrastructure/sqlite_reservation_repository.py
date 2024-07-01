from reservation.domain.reservation_repository import ReservationRepository
from reservation.infrastructure.reservation_entity import ReservationEntity


class SqliteReservationRepository(ReservationRepository):
    def create_reservation(self, reservation) -> int:
        reservation_entity = ReservationEntity.from_domain_model(reservation)
        reservation_entity.save()
        return reservation_entity.reservation_id

    def get_reservations_by_offer_id(self, offer_id: int) -> list:
        return [reservation.to_domain_model() for reservation in ReservationEntity.select().where(ReservationEntity.offer_id == offer_id)]

    def get_reservations_by_user_id(self, user_id: int) -> list:
        return [reservation.to_domain_model() for reservation in ReservationEntity.select().where(ReservationEntity.user_id == user_id)]

    def delete_reservation(self, reservation_id: int):
        query = ReservationEntity.delete().where(ReservationEntity.reservation_id == reservation_id)
        query.execute()
