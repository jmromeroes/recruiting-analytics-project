from typing import Dict

from recruiting_analytics_backend.business.queries.base import NotFoundQueryException, BadRequestQueryException, InternalServerException
import requests

class TorreQuery:
    ROOT_URL = "https://torre.bio/api/"
    
    def get(self, uri: str, **kwargs) -> Dict:

        response = requests.get(TorreQuery.ROOT_URL + uri)

        if response.status_code == 200:
            return self._build_dto(response.json(), **kwargs)
        else:
            if response.status_code == 404:
                raise NotFoundQueryException()
            elif response.status_code == 400:
                raise BadRequestQueryException()
            else:
                raise InternalServerException()

    def _build_dto(self, response: Dict, **kwargs):
        raise NotImplementedError
