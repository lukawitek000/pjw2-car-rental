from abc import ABC, abstractmethod


class ReverseGeocodingClient(ABC):
    @abstractmethod
    def get_address(self, geo_coordinates):
        pass
