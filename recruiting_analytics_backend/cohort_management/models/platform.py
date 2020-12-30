import json

from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

import datetime

class Platform(models.Model):
    name=models.CharField(max_length=50)
    url=models.CharField(max_length=100)
