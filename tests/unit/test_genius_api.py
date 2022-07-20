from unittest import TestCase
from unittest.mock import patch

from services.genius_api import Genius


class MockResponse:
    def __init__(self, valid=True, *args, **kwargs):
        self.valid = valid

    def json(self, *args, **kwargs):
        return {
            "response": {
                "hits": [{"song": "valid_song"}]
            }
        }


class TestGeniusSearch(TestCase):
    def setUp(self) -> None:
        self.api = Genius()
        self.valid_search = 'Valid search string'

    @patch('services.genius_api.requests.get')
    def test_search_should_return_when_data_is_found(self, mock):
        mock.return_value = MockResponse()
        response = self.api.search(self.valid_search)
        self.assertEqual(response, {
            "response": {
                "hits": [{"song": "valid_song"}]
            }
        })
