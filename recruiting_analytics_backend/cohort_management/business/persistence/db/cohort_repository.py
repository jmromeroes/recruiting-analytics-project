import json

from typing import List

from django.contrib.auth.models import User

from cohort_management.models.cohort import Cohort, Organization
from cohort_management.models.platform import Platform
from recruiting_analytics_backend.business.repositories.base import NotFoundRepositoryException, RepositoryException
from cohort_management.business.domain.cohort.cohort_information import CohortInformation


class CohortRepository:

    @staticmethod
    def list_cohorts_by_username(manager_username: str) -> List[CohortInformation]:
        try:
            user = User.objects.get(username=manager_username)
            manager = Manager.objects.get(user=user)

            return list(map(lambda cohort: cohort.to_domain(), manager.cohorts))
        except User.DoesNotExist:
            return NotFoundRepositoryException("User with username '{}' was not found in the database".format(username))
        except Manager.DoesNotExist:
            return NotFoundRepositoryException("Manager with username '{}' was not found in the database".format(username))
        except Exception as e:
            return RepositoryException(e)

    @staticmethod
    def create_or_update_cohort(cohort_information: CohortInformation) -> CohortInformation:
        try:
            cohort_exists = Cohort.objects.filter(
                id=cohort_information.id).exists()

            if cohort_exists:
                cohort_db = Cohort()
            else:
                cohort_db = Cohort.objects.get(id=cohort_information.id)

            cohort_db.name = cohort_information.name
            cohort_db.platform = Platform.objects.get(
                name=cohort_information.platform_name)
            cohort_db.platform_opportunity_id = cohort_information.opportunity_id
            cohort_db.opportunity_objective = cohort_information.opportunity_objective
            cohort_db.organization = Organization.objects.get_or_create(name=cohort_information.organization.name, picture=cohort_information.organization.picture)
            cohort_db.slug = cohort_information.slug
        except Platform.DoesNotExist:
            return NotFoundRepositoryException("Platform with name '{}' was not found in the database".format(cohort_information.platform_name))
