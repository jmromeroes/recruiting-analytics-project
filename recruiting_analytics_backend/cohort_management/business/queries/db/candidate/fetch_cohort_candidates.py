from typing import Dict, List

from cohort_management.business.persistence.db.candidate_repository import CandidateRepository
from cohort_management.business.domain.candidate.candidate_information import CandidateInformation

class FetchCohortCandidates:
    def execute(self, cohort_id: int) -> List[CandidateInformation]:
        return CandidateRepository.list_cohort_candidates(cohort_id)
