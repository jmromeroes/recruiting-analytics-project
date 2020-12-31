from typing import Dict, List

from cohort_management.business.persistence.db.cohort_repository import CohortRepository
from cohort_management.business.domain.cohort.cohort_information import CohortInformation
from recruiting_analytics_backend.business.commands.base import CommandBase

class CreateNewCohort(CommandBase):
    def execute(self, cohort_information: CohortInformation, user) -> CohortInformation:
        return CohortRepository.create_cohort(cohort_information, user)
