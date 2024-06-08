from abc import ABC, abstractmethod

from location.domain.geo_coordinates import GeoCoordinates


class GeocodingClient(ABC):
    @abstractmethod
    def get_coordinates(self, address) -> GeoCoordinates:
        """
        Get the geographical coordinates (latitude and longitude) for a given address.

        Parameters:
        address (str): The address to geocode.

        Returns:
        GeoCoordinates: The geographical coordinates of the address.

        Raises:
        GeocodingRequestFailed: If the request to the geocoding API fails. This could be due to network issues, server issues, or issues with the request itself (such as an invalid API key).
        NoResultsFoundForAddressException: If the geocoding API returns a successful response, but there are no results for the provided address. This could be because the address is invalid, or because it's a very remote location that isn't covered by the geocoding API.

        """
        pass
