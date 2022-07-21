from functools import lru_cache

from pydantic import BaseSettings, Field


WEEK_IN_SECONDS = 604_800


class Settings(BaseSettings):
    # GENIUS API
    GENIUS_ACCESS_TOKEN: str = Field(...)
    GENIUS_BASE_URL: str = Field(...)

    # DYNAMO
    DYNAMO_URI: str = Field(default=None)
    DYNAMO_REGION: str = Field(default='us-east-1')

    # REDIS
    REDIS_HOST: str = Field(...)
    REDIS_PORT: int = Field(...)
    REDIS_PASSWORD: str = Field(...)
    REDIS_EXPIRE_CACHE: int = Field(default=WEEK_IN_SECONDS)

    class Config:
        env_file = '.env'


@lru_cache
def get_config() -> Settings:
    return Settings()
