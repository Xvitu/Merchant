from merchant import create_app


class TestFactory:

    def test_config(self):
        assert not create_app().testing
        assert create_app({'TESTING': True}).testing

    def test_health(self, client):
        response = client.get('/health')
        assert response.data == b'Got some rare things on sale, stranger!'