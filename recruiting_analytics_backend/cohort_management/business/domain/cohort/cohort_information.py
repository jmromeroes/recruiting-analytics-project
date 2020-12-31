import attr
from typing import List

from ..base import BaseValueObject


@attr.s(auto_attribs=True, frozen=True)
class OrganizationInformation(BaseValueObject):
    name: str
    picture: str


@attr.s(auto_attribs=True, frozen=True)
class CohortInformation(BaseValueObject):
    id: int
    name: str
    platform_name: str
    opportunity_objective: str
    opportunity_id: str
    organizations: List[OrganizationInformation]
    slug: str