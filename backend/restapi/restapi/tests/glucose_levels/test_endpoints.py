import pytest

pytestmark = pytest.mark.django_db


class TestLevelsEndpoints:
    user_id_endpoint = "/api/v1/levels/?&user_id={user_id}/"
    id_endpoint_template = "/api/v1/levels/{id}/"

    def test_detail_success(self, api_client, glucose_level_factory):
        # Arrange
        glucose_level = glucose_level_factory()
        id_endpoint = self.id_endpoint_template.format(id=glucose_level.id)
        # Act
        response = api_client().get(id_endpoint)
        # Assert
        assert response.status_code == 200
        assert response.data["id"] == glucose_level.id

    def test_detail_not_found(self, api_client):
        # Arrange
        non_existent_id = 999
        id_endpoint = self.id_endpoint_template.format(id=non_existent_id)
        # Act
        response = api_client().get(id_endpoint)
        # Assert
        assert response.status_code == 404

    def test_list_success(self, api_client, glucose_level_factory):
        # Arrange
        glucose_level = glucose_level_factory()
        user_id = glucose_level.user.user_id
        user_id_endpoint = self.user_id_endpoint.format(user_id=user_id)
        # Act
        response = api_client().get(user_id_endpoint)
        # Assert
        assert response.status_code == 200
