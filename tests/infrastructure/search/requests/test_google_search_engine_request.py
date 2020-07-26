from merchant.src.infrastructure.search.requests.google_search_engine_request import GoogleSearchEngineRequest


class TestGoogleSearchEngineRequest:

    def test_should_get_the_corrects_params_to_request(self):
        search = GoogleSearchEngineRequest("fake search")
        params = search.get_params()

        assert 'gl' in params
        assert 'key' in params
        assert 'cx' in params
        assert 'q' in params

        assert params.get('q') == 'fake search'
        assert params.get('gl') == 'br'

    def test_should_change_the_default_gl_param(self):
        search = GoogleSearchEngineRequest("fake search", 'us')
        params = search.get_params()

        assert 'gl' in params
        assert 'key' in params
        assert 'cx' in params
        assert 'q' in params

        assert params.get('q') == 'fake search'
        assert params.get('gl') == 'us'
