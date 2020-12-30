import attr
from typing import List

from ..base import BaseValueObject

from cohort_management.business.domain.cohort.cohort_information import OrganizationInformation

@attr.s(auto_attribs=True, frozen=True)
class LinkInformation(BaseValueObject):
    name: str
    url: str


@attr.s(auto_attribs=True, frozen=True)
class JobInformation(BaseValueObject):
    name: str
    organizations: List[OrganizationInformation]


@attr.s(auto_attribs=True, frozen=True)
class CandidateInformation(BaseValueObject):
    username: str
    country: str
    platform_name: str
    public_id: str
    bio: str
    strengths: List[str]
    interests: List[str]
    jobs: List[JobInformation]
    links: List[LinkInformation]
    cohort_id: int
    number_of_strengths: int
    number_of_awards: int
    number_of_jobs: int
    number_of_projects: int
    number_of_interests: int