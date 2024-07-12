import factory
from restapi.glucose_levels.models import User, GlucoseLevel


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    user_id = "aaa"


class GlucoseLevelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GlucoseLevel

    user = factory.SubFactory(UserFactory)
    device = "device"
    serial_number = "serial_number"
    device_timestamp = "2021-01-01T00:00:00Z"
    record_type = 1
    glucose_value_history = 100.0
