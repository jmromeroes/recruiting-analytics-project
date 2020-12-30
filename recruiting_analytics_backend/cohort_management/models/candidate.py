import json

from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

from cohort_management.models.platform import Platform
from cohort_management.models.cohort import Cohort, Organization

import datetime
from django_countries.fields import CountryField


class Candidate(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    complete_profile = models.BooleanField(default=False)
    verified = models.BooleanField(default=True)
    country = models.CharField(max_length=100)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    platform_user_id = models.CharField(blank=True, null=True, max_length=150)
    platform_username = models.CharField(max_length=100)
    platform_public_id = models.CharField(max_length=100)
    platform_candidate_bio = models.TextField(default="")
    strengths = models.PositiveIntegerField()
    awards = models.PositiveIntegerField()
    interests = models.PositiveIntegerField()
    jobs = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()


class Strength(models.Model):
    name = models.CharField(max_length=100)


class CandidateStrength(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    strength = models.ForeignKey(Strength, on_delete=models.CASCADE)


class Interest(models.Model):
    name = models.CharField(max_length=100)


class CandidateInterest(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)


class CandidateOrganization(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Job(models.Model):
    name = models.CharField(max_length=100)


class CandidateJob(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    
class CandidateLink(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    link = models.CharField(max_length=150)


class CandidateCohort(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
