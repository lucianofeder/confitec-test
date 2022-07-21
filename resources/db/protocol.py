from typing import Any, Dict, Protocol


class DB(Protocol):
    def __init__(self, client: Any) -> None:
        ...

    def put(
        self,
        table: str,
        item: Dict[str, Any]
    ) -> Dict[str, Any]:
        ...
