from django.urls import path

from cohort_management.views.cohort import CohortsAPI
from cohort_management.views.candidate import CandidatesAPI

urlpatterns = [
    path(
        "cohort/<cohort_id>/candidates/",
        CandidatesAPI.as_view(),
        name="candidates_view",
    ),
    path(
        "cohorts/",
        CohortsAPI.as_view(),
        name="cohorts_view",
    ),
]
