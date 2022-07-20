from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # GENIUS API
    GENIUS_ACCESS_TOKEN: str = Field(...)
    GENIUS_BASE_URL: str = Field(...)

    class Config:
        env_file = '.env'


@lru_cache
def get_config() -> Settings:
    return Settings()
