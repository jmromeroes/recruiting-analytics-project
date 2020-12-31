from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from cohort_management.business.queries.db.candidate.fetch_cohort_candidates import FetchCohortCandidates
from cohort_management.business.queries.db.cohort.fetch_manager_cohorts import ListManagerCohorts

from cohort_management.business.commands.db.cohort.create_new_cohort import CreateNewCohort
from cohort_management.business.queries.api.torre.cohort.fetch_cohort_information_by_id import FetchCohortInformationById

from recruiting_analytics_backend.business.repositories.base import NotFoundRepositoryException, DuplicatedRepositoryException
from recruiting_analytics_backend.business.queries.base import NotFoundQueryException, BadRequestQueryException, InternalServerException

import json

import logging 
_logger = logging.getLogger(__name__)

class CohortsAPI(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            query_result = ListManagerCohorts().execute(request.user.username)
            return Response(list(map(lambda res: res.to_json(), query_result)))
        except NotFoundRepositoryException as e:
            _logger.exception(e)
            return Response(
                {
                    "error": e
                },
                status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            _logger.exception(e)
            return Response(
                {"error": "Internal server error"},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        opportunity_id = request.data.get("opportunity_id", "")

        if not len(opportunity_id):
            return Response(
                {"error": "opportunity_id not found in body"},
                status.HTTP_400_BAD_REQUEST
            )

        try:
            cohort_information = FetchCohortInformationById().execute(opportunity_id)
            cohort_information = CreateNewCohort().execute(cohort_information, request.user)

            return Response(cohort_information.to_json())
        except NotFoundQueryException as e:
            _logger.exception(e)

            return Response(
                {
                    "error": "Opportunity with id {} was not found in the api".format(opportunity_id)},
                status.HTTP_404_NOT_FOUND
            )
        except DuplicatedRepositoryException as e:
            _logger.exception(e)

            return Response(
                {
                    "error": "Cohort with opportunity id {} already exists for this manager".format(opportunity_id)},
                status.HTTP_409_CONFLICT
            )
        except Exception as e:
            _logger.exception(e)

            return Response(
                {"error": "Internal server error"},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )