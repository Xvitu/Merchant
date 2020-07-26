import requests
import os
from merchant.src.infrastructure.search.requests.google_search_engine_request import GoogleSearchEngineRequest
from merchant.src.infrastructure.search.responses.product import Product


class GSEClient:
    def __init__(self):
        self.__api_url = os.getenv('GSE_API_URL')

    def get_products(self, request: GoogleSearchEngineRequest) -> {Product}:
        response = requests.get(url=self.__api_url, params=request.get_params())

        products = response.items.pagemap.product

