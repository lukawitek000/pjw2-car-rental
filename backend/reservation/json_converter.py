def reservation_to_dict(reservation):
    return {
        "reservation_id": reservation.reservation_id,
        "user_id": reservation.user_id,
        "offer_id": reservation.offer_id,
        "start_date_time": reservation.start_date_time,
        "end_date_time": reservation.end_date_time
    }