

class LocationService:
    def __init__(self, geocoding_client, reverse_geocoding_client, search_client):
        self.geocoding_client = geocoding_client
        self.reverse_geocoding_client = reverse_geocoding_client
        self.search_client = search_client

    def find_coordinates_for_address(self, address):
        return self.geocoding_client.get_coordinates(address)

    def find_address_for_coordinates(self, geo_coordinates):
        return self.reverse_geocoding_client.get_address(geo_coordinates)

    def find_auto_complete(self, query):
        return self.search_client.search(query)
