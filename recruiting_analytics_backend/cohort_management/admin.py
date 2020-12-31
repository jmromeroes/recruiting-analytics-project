from django.contrib import admin

# Register your models here.
from cohort_management.models.manager import Manager
from cohort_management.models.cohort import Cohort

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass

@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    pass