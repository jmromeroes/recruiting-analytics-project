from typing import Dict

from ..exceptions import NotFoundQueryException, BadRequestQueryException, InternalServerException
from django.conf import settings
import requests

class TorreQuery:
    ROOT_URL = "https://api.github.com/"
    HEADERS = { "Accept": "application/vnd.github.v3+json" }
    
    def get(self, uri: str) -> Dict:

        response = requests.get(GitHubQuery.ROOT_URL + uri, headers=GitHubQuery.HEADERS)

        if response.status_code == 200:
            return self._build_dto(response.json())
        else:
            if response.status_code == 404:
                raise NotFoundQueryException()
            elif response.status_code == 400:
                raise BadRequestQueryException()
            else:
                raise InternalServerException()

    def _build_dto(self, response: Dict):
        raise NotImplementedError
