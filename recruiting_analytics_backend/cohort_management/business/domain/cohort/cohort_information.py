import attr
from typing import List

from ..base import BaseValueObject


@attr.s(auto_attribs=True, frozen=True)
class OrganizationInformation(BaseValueObject):
    name: str
    picture: str


@attr.s(auto_attribs=True, frozen=True)
class CohortInformation(BaseValueObject):
    name: str
    platform_name: str
    opportunity_objective: str
    organization: OrganizationInformation
    url: str