from django.contrib import admin

# Register your models here.
from cohort_management.models.manager import Manager
from cohort_management.models.cohort import Cohort
from cohort_management.models.platform import Platform
from cohort_management.models.candidate import Candidate

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass

@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    pass

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    pass

@admin.register(Candidate)
class CandidatesAdmin(admin.ModelAdmin):
    pass