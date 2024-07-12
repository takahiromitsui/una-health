from datetime import datetime
from django.utils.timezone import make_aware
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from django.shortcuts import get_object_or_404

from .models import GlucoseLevel
from .serializers import GlucoseLevelSerializer


# Create your views here.
# class GlucoseLevelViewSet(viewsets.ViewSet):
#     queryset = GlucoseLevel.objects.all()

#     @extend_schema(
#         responses=GlucoseLevelSerializer,
#         parameters=[
#             OpenApiParameter(
#                 name="user_id",
#                 description="Filter by user ID",
#                 required=False,
#                 type=OpenApiTypes.STR,
#             ),
#             OpenApiParameter(
#                 name="start",
#                 description="Start timestamp for filtering",
#                 required=False,
#                 type=OpenApiTypes.DATETIME,
#             ),
#             OpenApiParameter(
#                 name="stop",
#                 description="Stop timestamp for filtering",
#                 required=False,
#                 type=OpenApiTypes.DATETIME,
#             ),
#         ],
#     )
#     def list(self, request):
#         user_id = request.query_params.get("user_id")
#         if user_id:
#             self.queryset = self.queryset.filter(user_id=user_id)
#         start = request.query_params.get("start")
#         stop = request.query_params.get("stop")
#         if start and stop:
#             start_date = make_aware(datetime.strptime(start, "%Y-%m-%dT%H:%M:%S"))
#             stop_date = make_aware(datetime.strptime(stop, "%Y-%m-%dT%H:%M:%S"))
#             self.queryset = self.queryset.filter(
#                 timestamp__range=(start_date, stop_date)
#             )
#         sort = request.query_params.get("sort", "timestamp")
#         self.queryset = self.queryset.order_by(sort)

#         serializer = GlucoseLevelSerializer(self.queryset, many=True)
#         return Response(serializer.data)


class GlucoseLevelViewSet(viewsets.ViewSet):

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
            )
        ],
    )
    def list(self, request):
        user_id = request.query_params.get("user_id")
        if user_id:
            queryset = GlucoseLevel.objects.filter(user__user_id=user_id).order_by(
                "device_timestamp"
            )
            if queryset.exists():
                serializer = GlucoseLevelSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return Response(
                    {"error": "No glucose levels found for the given user ID"},
                    status=404,
                )
        else:
            return Response({"error": "user_id parameter is required"}, status=400)
