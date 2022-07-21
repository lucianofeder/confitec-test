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
    def put(self, *args, **kwargs):
        ...


class MockApi:
    def search(self, valid=True, *args, **kwargs):
        return {
            "response": {
                "hits": [{"song": "valid_song"}]
            }
        } if valid else {}


class TestArtistControllerSearch(TestCase):
    def setUp(self) -> None:
        self.valid_input = {'name': 'valid_name'}
        self.invalid_input = {'q': 'wrong_input'}
        self.controller = ArtistController(db=MockDB(), api=MockApi())

    @patch('app.controllers.artist_controller.TransactionModel')
    def test_search_should_return_when_data_is_found(self, mock):
        mock.return_value = MockTransactionModel()
        response = self.controller.search(**self.valid_input)
        self.assertEqual(response, {
            "response": {
                "hits": [{"song": "valid_song"}]
            }
        })

    @patch('app.controllers.artist_controller.TransactionModel')
    def test_search_should_raise_when_data_does_not_contain_name(self, mock):
        mock.return_value = MockTransactionModel()
        self.assertRaises(BadRequest, self.controller.search, **self.invalid_input)
