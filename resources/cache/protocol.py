from typing import Any, Protocol


class Cache(Protocol):
    def __init__(self, client: Any) -> None:
        ...

    def set(self, key: str, value: Any, expires: int, *args, **kwargs) -> None:
        ...

    def get(self, key: str) -> Any:
        ...
