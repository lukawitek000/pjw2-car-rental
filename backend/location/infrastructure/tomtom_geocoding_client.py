from location.domain.geo_coordinates import GeoCoordinates
from location.domain.geocoding_client import GeocodingClient


class TomTomGeocodingClient(GeocodingClient):

    def __init__(self, api_key):
        self.api_key = api_key

    def get_coordinates(self, address) -> GeoCoordinates:
        return GeoCoordinates(40.748817, -73.985428)

