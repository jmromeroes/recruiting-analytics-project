import json

from typing import List

from django.contrib.auth.models import User

from cohort_management.models.cohort import Cohort, Organization
from cohort_management.models.platform import Platform
from cohort_management.models.manager import Manager

from recruiting_analytics_backend.business.repositories.base import NotFoundRepositoryException, RepositoryException, DuplicatedRepositoryException
from cohort_management.business.domain.cohort.cohort_information import CohortInformation


class CohortRepository:

    @staticmethod
    def list_cohorts_by_username(manager_username: str) -> List[CohortInformation]:
        try:
            user = User.objects.get(username=manager_username)
            manager = Manager.objects.get(user=user)

            return list(map(lambda cohort: cohort.to_domain(), manager.cohorts))
        except User.DoesNotExist:
            raise NotFoundRepositoryException("User with username '{}' was not found in the database".format(manager_username))
        except Manager.DoesNotExist:
            raise NotFoundRepositoryException("Manager with username '{}' was not found in the database".format(manager_username))
        except Exception as e:
            raise RepositoryException(e)

    @staticmethod
    def create_cohort(cohort_information: CohortInformation, user) -> CohortInformation:
        try:
            manager = Manager.objects.get(user=user)
            cohort_exists =  Cohort.objects.filter(
                name=cohort_information.name, owner=manager).exists()

            if cohort_exists:
                raise DuplicatedRepositoryException("Cohort with same name already exists")

            cohort_db = Cohort()
            cohort_db.name = cohort_information.name
            cohort_db.platform = Platform.objects.get(
                name=cohort_information.platform_name)
            cohort_db.platform_opportunity_id = cohort_information.opportunity_id
            cohort_db.opportunity_objective = cohort_information.opportunity_objective
            cohort_db.owner = manager

            if len(cohort_information.organizations):
                cohort_db.organization = Organization.objects.get_or_create(name=cohort_information.organizations[0].name, picture=cohort_information.organization.picture)
            
            cohort_db.slug = cohort_information.slug

            cohort_db.save()
            return cohort_db.to_domain()
        except Manager.DoesNotExist:
            raise NotFoundRepositoryException("Manager with user id '{}' was not found in the database".format(user.id))
        except Platform.DoesNotExist:
            raise NotFoundRepositoryException("Platform with name '{}' was not found in the database".format(cohort_information.platform_name))
        except Exception as e:
            raise RepositoryException(e)