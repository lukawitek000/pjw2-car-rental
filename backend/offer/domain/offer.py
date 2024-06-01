class Offer:
    def __init__(self, user_id, car, price_per_day, extra_features, start_date_time, end_date_time, pickup,
                 return_location, offer_id=None):
        self.user_id = user_id
        self.offer_id = offer_id
        self.car = car
        self.price_per_day = price_per_day
        self.extra_features = extra_features
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.pickup_location = pickup
        self.return_location = return_location

    def __str__(self):
        return f"User ID: {self.user_id}, Offer ID: {self.offer_id}, Car: {self.car}, Price Per Day: {self.price_per_day}, " \
                f"Extra Features: {self.extra_features}, Start Date Time: {self.start_date_time}, " \
                f"End Date Time: {self.end_date_time}, Pickup: {self.pickup_location}, Return Location: {self.return_location}"
