from unittest import TestCase
from unittest.mock import patch

from app.controllers.artist_controller import ArtistController
from werkzeug.exceptions import BadRequest


class MockTransactionModel:
    __tablename__ = 'table'

    def __init__(self, *args, **kwargs):
        pass

    def dict(*args, **kwargs):
        ...


class MockDB:
    put_callcount = 0

    def put(self, *args, **kwargs):
        ...


class MockCache:
    def __init__(self, valid=True, *args, **kwargs) -> None:
        self.valid = valid

    def set(self, *args, **kwargs):
        ...

    def get(self, *args, **kwargs):
        return {"hits": [{"song": "valid_song"}]} if self.valid else {}


class MockApi:
    search_callcount = 0

    def search(self, valid=True, *args, **kwargs):
        self.search_callcount += 1
        return {"hits": [{"song": "valid_song"}]} if valid else {}


class TestArtistControllerSearch(TestCase):
    def setUp(self) -> None:
        self.valid_input = {'name': 'valid_name'}
        self.invalid_input = {'q': 'wrong_input'}
        self.controller = ArtistController(db=MockDB(), api=MockApi(), cache=MockCache())
        self.valid_response = {
            "hits": [{"song": "valid_song"}],
            "artist_name": "valid_name"
        }

    @patch('app.controllers.artist_controller.TransactionModel')
    def test_search_should_return_when_data_is_found(self, mock):
        mock.return_value = MockTransactionModel()
        response = self.controller.search(**self.valid_input)
        self.assertEqual(response, self.valid_response)

    @patch('app.controllers.artist_controller.TransactionModel')
    def test_search_should_raise_when_data_does_not_contain_name(self, mock):
        mock.return_value = MockTransactionModel()
        self.assertRaises(BadRequest, self.controller.search, **self.invalid_input)

    @patch('app.controllers.artist_controller.TransactionModel')
    def test_search_should_not_request_api_when_value_is_cached_and_cache_arg_is_true(self, mock):
        mock.return_value = MockTransactionModel()
        response = self.controller.search(**self.valid_input)
        self.assertEqual(self.controller.api.search_callcount, 0)
        self.assertEqual(response, self.valid_response)

    @patch('app.controllers.artist_controller.TransactionModel')
    def test_search_should_request_api_when_value_is_cached_and_cache_arg_is_false(self, mock):
        mock.return_value = MockTransactionModel()
        response = self.controller.search(name='valid_name', cache='False')
        self.assertEqual(self.controller.api.search_callcount, 1)
        self.assertEqual(response, self.valid_response)

    @patch('app.controllers.artist_controller.TransactionModel')
    def test_search_should_request_api_when_value_is_not_cached(self, mock):
        mock.return_value = MockTransactionModel()
        self.controller.cache.valid = False
        response = self.controller.search(**self.valid_input)
        self.assertEqual(self.controller.api.search_callcount, 1)
        self.assertEqual(response, self.valid_response)
