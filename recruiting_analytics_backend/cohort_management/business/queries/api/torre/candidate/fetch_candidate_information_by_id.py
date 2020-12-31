from ..torre_query import TorreQuery

from typing import Dict, List

from cohort_management.business.domain.candidate.candidate_information import CandidateInformation, JobInformation, LinkInformation
from cohort_management.business.domain.cohort.cohort_information import OrganizationInformation

class FetchCandidateById(TorreQuery):
    def execute(self, candidate_id: str, **kwargs) -> CandidateInformation:
        return self.get(TorreQuery.ROOT_URL_BIO + "bios/" + candidate_id, **kwargs)

    def _build_organization_dto(self, organization: Dict) -> OrganizationInformation:
        return OrganizationInformation(
            name=organization["name"],
            picture=organization.get("picture", "no-picture")
        )

    def _build_job_dto(self, job: Dict) -> JobInformation: 
        return JobInformation(
            name=job["name"],
            organizations=list(map(self._build_organization_dto, job["organizations"]))
        )

    def _build_link_dto(self, link: Dict) -> LinkInformation:
        return LinkInformation(
            name=link["name"],
            url=link.get("address", "")
        )

    def _build_dto(self, response: Dict, **kwargs) -> CandidateInformation:
        print(response)
        return CandidateInformation(
            username=response["person"].get("name", ""),
            country=response["person"]["location"]["country"] if "location" in response["person"] else "No Country",
            platform_name="Torre",
            public_id=response["person"]["publicId"],
            bio=response.get("summaryOfBio", ""),
            strengths=list(map(lambda strength: strength["name"], response.get("strengths", []))),
            interests=list(map(lambda interest: interest["name"], response.get("interests", []))),
            jobs=list(map(self._build_job_dto, response.get("jobs", []))),
            links=list(map(self._build_link_dto, response.get("strengths", []))),
            number_of_strengths=response["stats"].get("strengths", 0),
            number_of_awards=response["stats"].get("awards", 0),
            number_of_interests=response["stats"].get("interests", 0),
            number_of_jobs=response["stats"].get("jobs", 0),
            number_of_projects=response["stats"].get("projects", 0),
            cohort_id=kwargs["cohort_id"]
        )
