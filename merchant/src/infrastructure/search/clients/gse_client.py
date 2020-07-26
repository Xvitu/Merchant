import requests
import os
from merchant.src.infrastructure.search.requests.google_search_engine_request import GoogleSearchEngineRequest
from merchant.src.domain.entities.product import Product
from merchant.src.infrastructure.search.responses.search_result import SearchResult
from settings import GSE_API_URL

class GSEClient:
    def __init__(self):
        self.__api_url = GSE_API_URL

    def get_products(self, request: GoogleSearchEngineRequest) -> {Product}:
        response = requests.get(url=self.__api_url, params=request.get_params())

        return SearchResult(response.json())
