import json

from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

from cohort_management.models.platform import Platform
from cohort_management.models.cohort import Cohort, Organization

import datetime
from django_countries.fields import CountryField

from cohort_management.business.domain.candidate.candidate_information import CandidateInformation, LinkInformation


class Strength(models.Model):
    name = models.CharField(max_length=100)


class Interest(models.Model):
    name = models.CharField(max_length=100)


class Job(models.Model):
    name = models.CharField(max_length=100)


class Candidate(models.Model):
    complete_profile = models.BooleanField(default=False)
    verified = models.BooleanField(default=True)
    country = models.CharField(max_length=100)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    platform_user_id = models.CharField(blank=True, null=True, max_length=150)
    platform_username = models.CharField(max_length=100)
    platform_public_id = models.CharField(max_length=100)
    platform_candidate_bio = models.TextField(default="")
    number_of_strengths = models.PositiveIntegerField()
    number_of_awards = models.PositiveIntegerField()
    number_of_interests = models.PositiveIntegerField()
    number_of_jobs = models.PositiveIntegerField()
    number_of_projects = models.PositiveIntegerField()
    strengths = models.ManyToManyField(Strength)
    interests = models.ManyToManyField(Interest)
    organizations = models.ManyToManyField(Organization)
    jobs = models.ManyToManyField(Job)

    def to_domain(self) -> CandidateInformation:
        links = CandidateLink.objects.filter(candidate=self)

        return CandidateInformation(
            username=self.platform_username,
            country=self.country,
            platform_name=self.platform.name,
            public_id=self.platform_public_id,
            bio=self.platform_candidate_bio,
            strengths=list(
                map(lambda strength: strength.name, self.strengths)),
            interests=list(
                map(lambda interest: interest.name, self.interests)),
            previous_organizations=list(
                map(lambda organization: organization.to_domain(), self.organizations)),
            links=list(
                map(lambda link: link.to_domain(), links))
        )


class CandidateLink(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    link = models.CharField(max_length=150)

    def to_domain(self):
        return LinkInformation(
            name=self.name,
            url=self.url
        )