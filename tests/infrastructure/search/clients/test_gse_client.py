from merchant.src.infrastructure.search.clients.gse_client import GSEClient
from merchant.src.infrastructure.search.requests.google_search_engine_request import GoogleSearchEngineRequest
import json
import os


class TestGSEClient:

    def test_should_get_result_from_a_search(self, requests_mock):
        json_content = self.__get_json_content()
        requests_mock.get("https://www.googleapis.com/customsearch/v1", json=json_content, status_code=200)

        gse_request = GoogleSearchEngineRequest("fake search")
        client = GSEClient()
        response = client.get_products(gse_request)

        assert json_content.get('items') == response.items

    @staticmethod
    def __get_json_content():
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'google_search_response_mock.json')
        with open(my_file) as json_file:
            return json.load(json_file)
