from typing import Dict, List

from cohort_management.business.persistence.db.candidate_repository import CandidateRepository
from cohort_management.business.domain.candidate.candidate_information import CandidateInformation

from recruiting_analytics_backend.business.commands.base import CommandBase
class AddCandidateToCohort(CommandBase):
    def execute(self, candidate_information: CandidateInformation) -> CandidateInformation:
        return CandidateRepository.add_candidate(candidate_information)
