from abc import ABC, abstractmethod
from typing import List


class SearchClient(ABC):
    @abstractmethod
    def search(self, query: str) -> List[str]:
        pass
