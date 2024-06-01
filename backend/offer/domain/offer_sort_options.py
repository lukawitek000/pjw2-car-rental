from enum import Enum


class OfferSortOptions:
    def __init__(self, sort_by_price=None):
        self.sort_by_price = SortByPrice(sort_by_price) if sort_by_price else None


class SortByPrice(Enum):
    FROM_LOWEST = 'from_lowest'
    FROM_HIGHEST = 'from_highest'
