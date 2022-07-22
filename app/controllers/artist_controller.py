from http import HTTPStatus
from typing import Any, Dict

from app.models.transaction import TransactionModel
from app.schemas.artist_schemas import ArtistRetrieveSchema
from flask import abort
from resources.cache.protocol import Cache
from resources.cache.redis import get_cache_instance
from resources.db.dynamo import get_db
from resources.db.protocol import DB
from services.genius_api import Genius


class ArtistController:
    def __init__(
        self,
        db: DB = get_db(),
        api: Genius = Genius(),
        cache: Cache = get_cache_instance()
    ) -> None:
        self.db = db
        self.api = api
        self.cache = cache

    def search(self, **arguments) -> Dict[str, Any]:
        """Searchs an artist by name from external api, and handles it with
        cache for better performance

        Returns:
            Dict[str, Any]: a normalized response from the api with artist
            hits and name
        """
        if 'name' not in arguments.keys():
            abort(
                HTTPStatus.BAD_REQUEST,
                description='Missing name query parameter'
            )
        artist_name = arguments.get('name')
        use_cache = arguments.get('cache', True)
        transaction = TransactionModel(artist=artist_name, cache=use_cache)
        cached_value = self.cache.get(artist_name)
        if use_cache != 'False' and cached_value:
            self.db.put(transaction.__tablename__, transaction.dict())
            return ArtistRetrieveSchema(
                artist_name=artist_name,
                hits=cached_value.get('hits', [])
            ).dict()

        response = self.api.search(artist_name)
        if use_cache != 'False':
            self.cache.set(artist_name, response)
            self.db.put(transaction.__tablename__, transaction.dict())
        else:
            self.db.put(transaction.__tablename__, transaction.dict())
        return ArtistRetrieveSchema(
            artist_name=artist_name,
            hits=response.get('hits', [])
        ).dict()
