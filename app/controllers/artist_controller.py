from http import HTTPStatus

from app.models.transaction import TransactionModel
from flask import abort
from resources.db.dynamo import get_db
from resources.db.protocol import DB
from services.genius_api import Genius


class ArtistController:
    def __init__(
        self,
        db: DB = get_db(),
        api: Genius = Genius(),
    ) -> None:
        self.db = db
        self.api = api

    def search(self, **arguments):
        if 'name' not in arguments.keys():
            abort(
                HTTPStatus.BAD_REQUEST,
                description='Missing name query parameter'
            )
        artist_name = arguments.get('name')
        transaction = TransactionModel(artist=artist_name)
        response = self.api.search(artist_name)
        self.db.put(transaction.__tablename__, transaction.dict())
        return response
