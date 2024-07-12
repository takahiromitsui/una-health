import pytest

pytestmark = pytest.mark.django_db


class TestUserModel:
    def test_str_method(self, user_factory):
        # Arrange
        # Act
        user = user_factory()
        # Assert
        assert user.__str__() == "aaa"

class TestGlucoseLevelModel:
    def test_str_method(self, glucose_level_factory):
        # Arrange
        # Act
        glucose_level = glucose_level_factory()
        # Assert
        assert glucose_level.__str__() == 100.0