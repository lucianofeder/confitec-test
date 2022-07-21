from functools import lru_cache
from typing import Any, Dict

import boto3
from resources.configs import get_config

client = boto3.resource(
    'dynamodb',
    endpoint_url=get_config().DYNAMO_URI,
    region_name='us-east-1'
)


class Dynamo:
    def __init__(self, client) -> None:
        self.client = client

    def put(
        self,
        table: str,
        item: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Save an item, if the id has already been registered, the item will be edited.

        Args:
            table (str): table name.
            item (Dict[str, Any]): data to be saved

        Returns:
            Dict[str, Any]: A dict containing the data found.
        """
        response = self.client.Table(table).put_item(Item=item)
        return response


@lru_cache
def get_db() -> Dynamo:
    """Returns an Instance of Dynamo

    Returns:
        Dynamo instance
    """
    global client
    return Dynamo(client)
