import json

from typing import List

from cohort_management.models.manager import ManagerCohort, Manager
from django.contrib.auth.models import User

class CohortRepository:

    @staticmethod
    def list_manager_cohorts(username: str):
        try:    
            user = User.objects.get(username)
            manager_cohort = 
            owner = GithubUser.objects.get(login=username)
            repositories = list(map(lambda u: u["fields"], json.loads(serializers.serialize("json", Repository.objects.filter(owner=owner)))))
            domain_repositories = cattr.structure(repositories, List[RepositoryInformation])

            return domain_repositories
                
            
