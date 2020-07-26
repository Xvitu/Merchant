import json
from merchant.src.infrastructure.search.clients.gse_client import GSEClient
from merchant.src.infrastructure.search.requests.google_search_engine_request import GoogleSearchEngineRequest
import os

def test_read():
    with open("google_search_response_mock.json") as file_json:
        json_content = json.load(file_json)

    print(json_content)

def test_product():
    request = GoogleSearchEngineRequest('smartphone')
    client = GSEClient()
    response = client.get_products(request)

