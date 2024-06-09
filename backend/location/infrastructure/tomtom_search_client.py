from typing import List

import requests

from location.domain.search_client import SearchClient
from location.domain.search_exceptions import SearchFailedException


class TomTomSearchClient(SearchClient):

    __base_url = "https://api.tomtom.com/search/2/search/"

    def __init__(self, api_key: str):
        self.__api_key = api_key

    def search(self, query: str) -> List[str]:
        complete_url = f"{self.__base_url}{query}.json"
        params = {
            "key": self.__api_key,
            "typeahead": "true",
            "minFuzzyLevel": 1,
            "maxFuzzyLevel": 2,
            "idxSet": "PAD,Addr,Str,Xstr",
            "view": "Unified",
            "relatedPois": "off"
        }
        response = requests.get(complete_url, params=params)

        if response.status_code != 200:
            raise SearchFailedException(f"Request failed with status code {response.status_code}")

        data = response.json()
        results = data["results"]

        if not results:
            raise SearchFailedException(f"No results found for query: {query}")
        return [result["address"]["freeformAddress"] for result in results]
