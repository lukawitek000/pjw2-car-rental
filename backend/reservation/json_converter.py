from offer.json_converter import car_to_dict


def reservation_to_dict(reservation):
    return {
        "reservation_id": reservation.reservation_id,
        "user_id": reservation.user_id,
        "offer_id": reservation.offer_id,
        "start_date_time": reservation.start_date_time,
        "end_date_time": reservation.end_date_time,
        "car": car_to_dict(reservation.car)
    }