from functools import lru_cache
from typing import Any

from resources.configs import get_config

from redis import Redis as RedisClient

settings = get_config()


client = RedisClient(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD
)


class Redis:
    def __init__(self, client: RedisClient):
        self.client = client

    def set(
        self,
        key: str,
        value: Any,
        expires: int = settings.REDIS_EXPIRE_CACHE,
        *args,
        **kwargs
    ) -> None:
        """Sets a value into cache

        Args:
            key (str): the key to access the value
            value (Any): value to be stored
            expires (int, optional): time in seconds to expire the cache, defaults to 7 days.
        """
        self.client.set(key, value, ex=expires, *args, **kwargs)

    def get(self, key: str) -> Any:
        """Gets the value store in cache

        Args:
            key (str): value to be searched

        Returns:
            Any: Returns the value stored or None if doesn't exist
        """
        return self.client.get(key)


@lru_cache
def get_cache_instance() -> Redis:
    global client
    return Redis(client=client)
