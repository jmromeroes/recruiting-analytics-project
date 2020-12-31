from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cohort_management.business.queries.db.candidate.fetch_cohort_candidates import FetchCohortCandidates
from cohort_management.business.queries.db.candidate.fetch_candidate import FetchCandidate
from cohort_management.business.queries.api.torre.candidate.fetch_candidate_information_by_id import FetchCandidateById
from cohort_management.business.commands.db.candidate.add_candidate_to_cohort import AddCandidateToCohort

from recruiting_analytics_backend.business.queries.base import NotFoundQueryException, BadRequestQueryException, InternalServerException

from recruiting_analytics_backend.business.repositories.base import NotFoundRepositoryException, RepositoryException, DuplicatedRepositoryException

import json

import logging 
_logger = logging.getLogger(__name__)

class CandidatesAPI(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, cohort_id):
        try:
            query_result = FetchCohortCandidates().execute(cohort_id)
            return Response(list(map(lambda cdt: cdt.to_json(), query_result)))
        except NotFoundRepositoryException as e:
            _logger.exception(e)

            return Response(
                {
                    "error": "Some resource was not found"},
                status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            _logger.exception(e)

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
        except NotFoundRepositoryException as e:
            _logger.exception(e)

            try:
                candidate = FetchCandidateById().execute(public_id, cohort_id=cohort_id)
                candidate = AddCandidateToCohort().execute(candidate)
            except NotFoundQueryException as e:
                _logger.exception(e)

                return Response(
                    {
                        "error": "Candidate with id {} was not found in the api".format(public_id)},
                    status.HTTP_404_NOT_FOUND
                )
            except DuplicatedRepositoryException as e:
                _logger.exception(e)

                return Response(
                    {
                        "error": "Candidate with id {} already exists in the cohort with id {}".format(public_id, cohort_id)},
                    status.HTTP_409_CONFLICT
                )
            except Exception as e:
                _logger.exception(e)

                return Response(
                    {"error": "Internal server error"},
                    status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        return Response(
            candidate.to_json()
        )
