from typing import Any, Dict

import requests
from resources.configs import get_config

settings = get_config()


class Genius:
    """Class that is responsible to communicate with Genius Api
    """
    __token = settings.GENIUS_ACCESS_TOKEN
    __base_url = settings.GENIUS_BASE_URL

    def search(self, data_to_search: str) -> Dict[str, Any]:
        """Makes a request to the endpoint '/search' of the api

        Args:
            data_to_search (str): A string containing what to search

        Returns:
           Dict[str, Any]:  Response containing what was found
        """
        response = requests.get(
            f'{self.__base_url}/search',
            {'q': data_to_search},
            headers={'Authorization': f'Bearer {self.__token}'}
        )
        return response.json()
