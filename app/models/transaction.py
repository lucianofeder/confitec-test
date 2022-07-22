from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


class TransactionModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    artist: str
    cache: bool = Field(default=True)

    __tablename__ = 'transaction'
