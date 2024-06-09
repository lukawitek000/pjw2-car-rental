import requests

from location.domain.reverse_geocoding_client import ReverseGeocodingClient
from location.domain.reverse_geocoding_exceptions import ReverseGeocodingFailedException, NoResultsFoundForCoordinates


class TomTomReverseGeocodingClient(ReverseGeocodingClient):

    __base_url = "https://api.tomtom.com/search/2/reverseGeocode/"

    def __init__(self, api_key):
        self.__api_key = api_key

    def get_address(self, geo_coordinates):
        complete_url = f"{self.__base_url}{geo_coordinates.latitude},{geo_coordinates.longitude}.json"
        params = {"key": self.__api_key}
        response = requests.get(complete_url, params=params)
        data = response.json()
        if response.status_code != 200:
            raise ReverseGeocodingFailedException(f"Request failed with status code {response.status_code}")
        if not data["addresses"]:
            raise NoResultsFoundForCoordinates(f"No results found for coordinates: {geo_coordinates}")
        return data["addresses"][0]["address"]["freeformAddress"]

