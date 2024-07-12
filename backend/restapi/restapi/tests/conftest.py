from pytest_factoryboy import register

from .factories import UserFactory, GlucoseLevelFactory

register(UserFactory)
register(GlucoseLevelFactory)
