import json

from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

import datetime

class Manager(models.Model):
    agreed_terms_and_conditions = models.BooleanField(default=False)
    terms_and_conditions_date = models.DateTimeField(
        default=datetime.datetime(2015, 2, 21, 19, 38, 32, 209148)
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )