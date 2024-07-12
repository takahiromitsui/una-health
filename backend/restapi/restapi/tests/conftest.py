from rest_framework.test import APIClient
import pytest
from pytest_factoryboy import register

from .factories import UserFactory, GlucoseLevelFactory

register(UserFactory)
register(GlucoseLevelFactory)

@pytest.fixture
def api_client():
    return APIClient