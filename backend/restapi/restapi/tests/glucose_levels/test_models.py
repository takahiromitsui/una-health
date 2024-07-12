import pytest

pytestmark = pytest.mark.django_db


class TestUserModel:
    def test_str_method(self, user_factory):
        # Arrange
        # Act
        user = user_factory()
        # Assert
        assert user.__str__() == "aaa"
