class Reservation:
    def __init__(self, user_id, offer_id, start_date_time, end_date_time, reservation_id=None):
        self.user_id = user_id
        self.offer_id = offer_id
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.reservation_id = reservation_id
        self.car = None

    def __str__(self):
        return f"Reservation ID: {self.reservation_id}, User ID: {self.user_id}, Offer ID: {self.offer_id}, " \
               f"Start: {self.start_date_time}, End: {self.end_date_time}"