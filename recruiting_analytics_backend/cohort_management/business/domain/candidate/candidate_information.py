import attr
from typing import List

from ..base import BaseValueObject

from cohort_management.business.domain.cohort.cohort_information import OrganizationInformation

@attr.s(auto_attribs=True, frozen=True)
class LinkInformation(BaseValueObject):
    name: str
    url: str


@attr.s(auto_attribs=True, frozen=True)
class CandidateInformation(BaseValueObject):
    username: str
    country: str
    platform_name: str
    public_id: str
    bio: str
    strengths: List[str]
    interests: List[str]
    jobs: List[str]
    links: List[LinkInformation]
    previous_organizations: List[OrganizationInformation]
