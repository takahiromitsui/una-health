from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import GlucoseLevel
from .serializers import GlucoseLevelSerializer


# Create your views here.
class GlucoseLevelViewSet(viewsets.ModelViewSet):
    queryset = GlucoseLevel.objects.all()

    @extend_schema(responses=GlucoseLevelSerializer)
    def list(self, request):
        serializer = GlucoseLevelSerializer(self.queryset, many=True)
        return Response(serializer.data)
