class OfferFilterByLocation:
    def __init__(self, all_offers, pickup_location, return_location, radius_km):
        self.all_offers = all_offers
        self.pickup_location = pickup_location
        self.return_location = return_location
        self.radius_km = radius_km

    def filter_offers(self):
        offers_in_radius = []

        for offer in self.all_offers:
            if (offer.pickup_location.is_within_radius(self.pickup_location, self.radius_km) and
                    offer.return_location.is_within_radius(self.return_location, self.radius_km)):
                offers_in_radius.append(offer)

        return offers_in_radius
