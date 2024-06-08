from abc import ABC, abstractmethod

from location.domain.geo_coordinates import GeoCoordinates


class GeocodingClient(ABC):
    @abstractmethod
    def get_coordinates(self, address) -> GeoCoordinates:
        pass