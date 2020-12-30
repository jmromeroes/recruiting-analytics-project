from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from cohort_management.business.queries.db.candidate.fetch_cohort_candidates import FetchCohortCandidates

from recruiting_analytics_backend.business.repositories.base import NotFoundRepositoryException

import json


class CohortAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, cohort_id):
        try:
            query_result = FetchCohortCandidates().execute(cohort_id)
            return Response(list(map(lambda repo: repo.to_json(), query_result)))
        except NotFoundRepositoryException:
            return Response(
                {
                    "error": "Some resource was not found"},
                status.HTTP_400_NOT_FOUND
            )
        except Exception:
            return Response(
                {"error": "Internal server error"},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
