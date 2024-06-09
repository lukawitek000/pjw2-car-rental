from math import radians, sin, cos, atan2, sqrt


class GeoCoordinates:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"

    def distance_to(self, other):
        # Radius of the Earth in km
        R = 6371.0

        lat1 = radians(self.latitude)
        lon1 = radians(self.longitude)
        lat2 = radians(other.latitude)
        lon2 = radians(other.longitude)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return distance

    def is_within_radius(self, other, radius_km):
        return self.distance_to(other) <= radius_km
