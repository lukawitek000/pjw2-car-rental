
class GeoCoordinates:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"