from ..torre_query import TorreQuery

from typing import Dict, List

from cohort_management.business.domain.cohort.cohort_information import CohortInformation, OrganizationInformation

class FetchCohortInformationById(TorreQuery):
    def execute(self, opportunity_id: str, **kwargs) -> CohortInformation:
        return self.get("opportunities/" + opportunity_id, **kwargs)

    def _build_organization_dto(self, organization: Dict) -> OrganizationInformation:
        return OrganizationInformation(
            name=organization["name"],
            picture=organization.get("picture", "no-picture")
        )

    def _build_dto(self, cohort_information: Dict, **kwargs) -> CohortInformation:
        return CohortInformation(
            name=cohort_information.get("objective", ""),
            platform_name="Torre",
            opportunity_objective=cohort_information.get("objective", ""),
            opportunity_id=cohort_information.get("id", ""),
            organizations=list(map(self._build_organization_dto, cohort_information["organizations"])),
            slug=cohort_information["slug"]
        )