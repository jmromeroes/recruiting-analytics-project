import json

from typing import List

from django.contrib.auth.models import User

from cohort_management.models.manager import Manager
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