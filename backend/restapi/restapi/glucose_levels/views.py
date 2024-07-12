from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from django.shortcuts import get_object_or_404
from dateutil import parser

from .models import GlucoseLevel
from .serializers import GlucoseLevelSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "page_size"


class GlucoseLevelViewSet(viewsets.ViewSet):
    pagination_class = CustomPagination

    @extend_schema(
        responses=GlucoseLevelSerializer,
    )
    def retrieve(self, request, pk=None):
        queryset = GlucoseLevel.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = GlucoseLevelSerializer(item)
        return Response(serializer.data)

    @extend_schema(
        responses=GlucoseLevelSerializer,
        parameters=[
            OpenApiParameter(
                name="user_id",
                description="Filter by user ID",
                required=True,
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="start",
                description="Filter by start date",
                required=False,
                type=OpenApiTypes.DATE,
            ),
            OpenApiParameter(
                name="stop",
                description="Filter by end date",
                required=False,
                type=OpenApiTypes.DATE,
            ),
        ],
    )
    def list(self, request):
        user_id = request.query_params.get("user_id")
        start = request.query_params.get("start")
        stop = request.query_params.get("stop")

        if user_id:
            queryset = GlucoseLevel.objects.filter(user__user_id=user_id)

            if start:
                start = parser.parse(start)
                queryset = queryset.filter(device_timestamp__gte=start)

            if stop:
                stop = parser.parse(stop)
                queryset = queryset.filter(device_timestamp__lte=stop)

            queryset = queryset.order_by("device_timestamp")

            paginator = self.pagination_class()
            page = paginator.paginate_queryset(queryset, request)

            if page is not None:
                serializer = GlucoseLevelSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)
            else:
                return Response(
                    {"error": "No glucose levels found for the given user ID"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {"error": "user_id parameter is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
