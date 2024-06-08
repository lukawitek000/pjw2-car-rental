import requests

from location.domain.geo_coordinates import GeoCoordinates
from location.domain.geocoding_client import GeocodingClient
from location.domain.geocoding_exceptions import GeocodingRequestFailed, NoResultsFoundForAddressException


class TomTomGeocodingClient(GeocodingClient):

    base_url = "https://api.tomtom.com/search/2/geocode/"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_coordinates(self, address) -> GeoCoordinates:
        complete_url = f"{self.base_url}{address}.json"
        params = {"key": self.api_key}
        response = requests.get(complete_url, params=params)
        data = response.json()
        if response.status_code != 200:
            raise GeocodingRequestFailed(f"Request failed with status code {response.status_code}")

        if not data["results"]:
            raise NoResultsFoundForAddressException(f"No results found for address: {address}")
        latitude = data["results"][0]["position"]["lat"]
        longitude = data["results"][0]["position"]["lon"]
        return GeoCoordinates(latitude, longitude)
