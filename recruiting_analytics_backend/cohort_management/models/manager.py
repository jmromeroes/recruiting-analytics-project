import json

from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

from cohort_management.models.cohort import Cohort
import datetime

class Manager(models.Model):
    agreed_terms_and_conditions = models.BooleanField(default=False)
    terms_and_conditions_date = models.DateTimeField(
        default=datetime.datetime(2015, 2, 21, 19, 38, 32, 209148)
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )

class ManagerCohort(models.Model):
    candidate = models.ForeignKey(Manager, on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)