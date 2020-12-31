import json

from typing import List, Dict

from cohort_management.models.cohort import Cohort, Organization
from cohort_management.models.candidate import Candidate, Strength, Interest, Job, CandidateLink
from cohort_management.business.domain.candidate.candidate_information import CandidateInformation
from cohort_management.models.platform import Platform

from django.contrib.auth.models import User
from recruiting_analytics_backend.business.repositories.base import NotFoundRepositoryException, RepositoryException, DuplicatedRepositoryException

import logging 
_logger = logging.getLogger(__name__)

class CandidateRepository:

    @staticmethod
    def list_cohort_candidates(cohort_id: int) -> List[CandidateInformation]:
        try:
            cohort = Cohort.objects.get(id=cohort_id)
            candidates = Candidate.objects.filter(cohort=cohort)

            return list(map(lambda cohort: cohort.to_domain(), candidates))
        except Cohort.DoesNotExist:
            raise NotFoundRepositoryException("Cohort with id '{}' was not found in the database".format(cohort_id))
        except Exception as e:
            raise RepositoryException(e)

    @staticmethod
    def get_candidate_by_cohort_id_and_platform_user_id(cohort_id: str, platform_user_id: str) -> CandidateInformation:
        try:
            candidate = Candidate.objects.get(
                cohort_id=cohort_id, platform_user_id=platform_user_id)
            
            return candidate.to_domain()
        except Candidate.DoesNotExist as e:
            _logger.exception(e)
            raise NotFoundRepositoryException("Candidate with id '{}' was not found in the database".format(platform_user_id))
        except Exception as e:
            _logger.exception(e)
            raise RepositoryException(e)

    @staticmethod
    def add_candidate(candidate_information: CandidateInformation) -> CandidateInformation:
        try:
            print("heree1")
            platform = Platform.objects.get(
                name=candidate_information.platform_name)

            candidate_exists = Candidate.objects.filter(
                cohort_id=candidate_information.cohort_id, platform_user_id=candidate_information.public_id).exists()

            cohort = Cohort.objects.get(id=candidate_information.cohort_id)
            if candidate_exists:
                raise DuplicatedRepositoryException("Candidate already exists")

            candidate = Candidate()
            candidate.complete_profile = True
            candidate.verified = False
            candidate.country = candidate_information.country
            candidate.platform = platform
            candidate.platform_public_id = candidate_information.public_id
            candidate.platform_candidate_bio = candidate_information.bio
            candidate.number_of_awards = candidate_information.number_of_awards
            candidate.number_of_strengths = candidate_information.number_of_strengths
            candidate.number_of_interests = candidate_information.number_of_interests
            candidate.number_of_projects = candidate_information.number_of_projects
            candidate.number_of_jobs = candidate_information.number_of_jobs
            candidate.cohort = cohort
            candidate.save()

            strengths_list = []
            for strength in candidate_information.strengths:
                strengths_list.append(
                    Strength.objects.get_or_create(name=strength)[0].id)
            candidate.strengths.add(*strengths_list)

            interests_list = []
            for interest in candidate_information.interests:
                interests_list.append(
                    Interest.objects.get_or_create(name=interest)[0].id)
            candidate.interests.add(*interests_list)

            for job in candidate_information.jobs:
                organization_list = []
                job_db = Job()
                job_db.name = job.name
                job_db.candidate = candidate
                job_db.save()

                for organization in job.organizations:
                    organization_list.append(Organization.objects.get_or_create(
                        name=organization.name, picture=organization.picture)[0].id)
                job_db.organizations.add(*organization_list)

            for link in candidate_information.links:
                link_db = CandidateLink()
                link_db.name = link.name
                link_db.link = link.url
                link_db.candidate = candidate
                link_db.save()

            return candidate.to_domain()
        except Platform.DoesNotExist as e:
            _logger.exception(e)
            raise NotFoundRepositoryException("Platform with name '{}' was not found in the database".format(candidate_information.platform_name))
        except Exception as e:
            _logger.exception(e.__traceback__)
            raise RepositoryException(e)
