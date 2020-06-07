import json

def test_read():
    with open("google_search_response_mock.json") as file_json:
        json_content = json.load(file_json)

    print(json_content)
