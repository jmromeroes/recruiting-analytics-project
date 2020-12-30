import json

from typing import List

from cohort_management.models.cohort import Cohort, Organization
from cohort_management.models.candidate import Candidate, Strength, Interest, Job, CandidateLink
from cohort_management.business.domain.candidate.candidate_information import CandidateInformation
from cohort_management.models.platform import Platform

from django.contrib.auth.models import User
from recruiting_analytics_backend.business.repositories.base import NotFoundRepositoryException, RepositoryException


class CandidateRepository:

    @staticmethod
    def list_cohort_candidates(cohort_id: int) -> List[CandidateInformation]:
        try:
            cohort = Cohort.objects.get(id=cohort_id)
            candidates = Candidate.objects.filter(cohort=cohort)

            return list(map(lambda cohort: cohort.to_domain(), candidates))
        except Cohort.DoesNotExist:
            return NotFoundRepositoryException("Cohort with id '{}' was not found in the database".format(cohort_id))
        except Exception as e:
            return RepositoryException(e)


    @staticmethod
    def get_candidate_by_id(candidate_id: int) -> CandidateInformation:
        try:
            candidate = Candidate.objects.get(id=candidate_id)

            return candidate.to_domain()
        except Candidate.DoesNotExist:
            return NotFoundRepositoryException("Candidate with id '{}' was not found in the database".format(candidate_id))
        except Exception as e:
            return RepositoryException(e)

    @staticmethod
    def add_or_update_candidate(candidate_information: CandidateInformation) -> CandidateInformation:
        try:
            platform = Platform.objects.get(
                name=candidate_information.platform_name)

            candidate_exists = Candidate.objects.filter(
                id=candidate_information.id).exists()

            if candidate_exists:
                candidate = Candidate.objects.get(id=candidate_information.id)
                candidate.strengths.clear()
                candidate.interests.clear()
                candidate.jobs.clear()
                candidate.links.clear()
                candidate.previous_organizations.clear()
                Job.objects.filter(candidate=candidate).all().delete()
                CandidateLink.objects.filter(candidate=candidate).all().delete()
            else:
                candidate = Candidate()

            candidate.complete_profile = True
            candidate.verified = False
            candidate.country = candidate_information.country
            candidate.platform = platform
            candidate.platform_public_id = candidate_information.public_id
            candidate.platform_candidate_bio = candidate_information.bio

            candidate.save()

            strengths_list = []
            for strength in candidate_information.strengths:
                strengths_list.append(
                    Strength.objects.get_or_create(name=strength).id)
            candidate.strengths.add(*strengths_list)

            interests_list = []
            for interest in candidate_information.interests:
                interests_list.append(
                    Interest.objects.get_or_create(name=interest).id)
            candidate.interests.add(*interests_list)

            for job in candidate_information.jobs:
                organization_list = []
                job_db = Job()
                job_db.name = job.name
                job_db.candidate = candidate
                job_db.save()

                for organization in job.organizations:
                    organization_list.append(Organization.objects.get_or_create(
                        name=organization.name, picture=organization.picture).id)
                job_db.organizations.add(*organization_list)    

            for link in candidate_information.links:
                link_db = CandidateLink()
                link_db.name = link.name
                link_db.link = link.link
                link_db.candidate = candidate
                link_db.save()

            return candidate.to_domain()
        except Platform.DoesNotExist:
            return NotFoundRepositoryException("Platform with name '{}' was not found in the database".format(candidate_information.platform_name))
        except Exception as e:
            return RepositoryException(e)

    