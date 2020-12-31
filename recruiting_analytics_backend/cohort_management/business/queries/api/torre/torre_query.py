from typing import Dict

from recruiting_analytics_backend.business.queries.base import NotFoundQueryException, BadRequestQueryException, InternalServerException
import requests

class TorreQuery:
    ROOT_URL_CO = "https://torre.co/api/"
    ROOT_URL_BIO = "https://torre.bio/api/"

    def get(self, url: str, **kwargs) -> Dict:
        response = requests.get(url)

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
