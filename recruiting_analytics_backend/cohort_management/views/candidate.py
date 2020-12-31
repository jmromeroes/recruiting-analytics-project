from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from cohort_management.business.queries.db.candidate.fetch_cohort_candidates import FetchCohortCandidates
from cohort_management.business.queries.db.candidate.fetch_candidate import FetchCandidate
from cohort_management.business.queries.api.torre.candidate.fetch_candidate_information_by_id import FetchCandidateById
from cohort_management.business.commands.db.candidate.add_candidate_to_cohort import AddCandidateToCohort

from recruiting_analytics_backend.business.queries.base import NotFoundQueryException, BadRequestQueryException, InternalServerException

from recruiting_analytics_backend.business.repositories.base import NotFoundRepositoryException, DuplicatedRepositoryException

import json


class CandidatesAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, cohort_id):
        try:
            query_result = FetchCohortCandidates().execute(cohort_id)
            return Response(list(map(lambda repo: repo.to_json(), query_result)))
        except NotFoundRepositoryException:
            return Response(
                {
                    "error": "Some resource was not found"},
                status.HTTP_404_NOT_FOUND
            )
        except Exception:
            return Response(
                {"error": "Internal server error"},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request, cohort_id):
        public_id = request.data.get("public_id", "")

        if not len(public_id):
            return Response(
                {"error": "public_id not found in body"},
                status.HTTP_400_BAD_REQUEST
            )

        try:
            candidate = FetchCandidate().execute(cohort_id, public_id)
        except NotFoundRepositoryException:
            try:
                candidate = FetchCandidateById().execute(public_id, cohort_id=cohort_id)
                candidate = AddCandidateToCohort().execute(candidate)
            except NotFoundQueryException:
                return Response(
                    {
                        "error": "Candidate with id {} was not found in the api".format(public_id)},
                    status.HTTP_404_NOT_FOUND
                )
            except DuplicatedRepositoryException:
                return Response(
                    {
                        "error": "Candidate with id {} already exists in the cohort with id {}".format(public_id, cohort_id)},
                    status.HTTP_409_CONFLICT
                )
            except Exception:
                return Response(
                    {"error": "Internal server error"},
                    status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        return Response(
            candidate.to_json()
        )