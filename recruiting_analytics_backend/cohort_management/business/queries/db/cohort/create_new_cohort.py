from typing import Dict, List

from cohort_management.business.persistence.db.cohort_repository import CohortRepository
from cohort_management.business.domain.cohort.cohort_information import CohortInformation

class CreateNewCohort:
    def execute(self, cohort_information: CohortInformation) -> CohortInformation:
        return CohortRepository.create_or_update_cohort(cohort_information)
