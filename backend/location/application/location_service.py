

class LocationService:
    def __init__(self, geocoding_client):
        self.geocoding_client = geocoding_client

    def find_coordinates_for_address(self, address):
        return self.geocoding_client.get_coordinates(address)
