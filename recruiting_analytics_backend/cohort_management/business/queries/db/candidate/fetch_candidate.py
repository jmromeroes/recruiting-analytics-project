from typing import Dict, List

from cohort_management.business.persistence.db.candidate_repository import CandidateRepository
from cohort_management.business.domain.candidate.candidate_information import CandidateInformation

class FetchCandidate:
    def execute(self, cohort_id: str, platform_user_id: str) -> CandidateInformation:
        return CandidateRepository.get_candidate_by_cohort_id_and_platform_user_id(cohort_id, platform_user_id)
