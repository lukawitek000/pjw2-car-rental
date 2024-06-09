class OfferFilterOptions:
    def __init__(self, start_date_time=None, end_date_time=None, pickup_location=None, return_location=None, radius_km=None):
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.pickup_location = pickup_location
        self.return_location = return_location
        self.radius_km = radius_km
