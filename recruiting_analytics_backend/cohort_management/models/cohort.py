import json

from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from cohort_management.models.platform import Platform
from cohort_management.models.manager import Manager

import datetime

from cohort_management.business.domain.cohort.cohort_information import OrganizationInformation, CohortInformation


class Organization(models.Model):
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=200)

    def to_domain(self) -> OrganizationInformation:
        return OrganizationInformation(
            name=self.name,
            picture=self.picture
        )


class Cohort(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    platform_opportunity_id = models.CharField(max_length=100)
    opportunity_objective = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.CharField(max_length=200)
    owner = models.ForeignKey(Manager, on_delete=models.CASCADE)

    def to_domain(self) -> CohortInformation:
        return CohortInformation(
            name=self.name,
            platform_name=self.platform.name,
            opportunity_objective=self.opportunity_objective,
            opportunity_id=self.platform_opportunity_id,
            organizations=[self.organization.to_domain()] if self.organization else [],
            slug=self.slug
        )
