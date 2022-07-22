from typing import Any, List

from pydantic import BaseModel, Field


class ArtistRetrieveSchema(BaseModel):
    artist_name: str
    hits: List[Any] = Field(default=[])
