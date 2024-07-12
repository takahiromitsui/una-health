from rest_framework import serializers
from .models import User, GlucoseLevel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GlucoseLevelSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GlucoseLevel
        fields = "__all__"
