from typing import Dict, List

from cohort_management.business.persistence.db.cohort_repository import CohortRepository
from cohort_management.business.domain.cohort.cohort_information import CohortInformation

class ListManagerCohorts:
    def execute(self, username: str) -> List[CohortInformation]:
        return CohortRepository.list_cohorts_by_username(username)
