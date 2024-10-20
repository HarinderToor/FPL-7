from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient


class APITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.MOCK_FPL_DATA = {
            "elements": [
                {"id": 1, "first_name": "John", "second_name": "Doe", "total_points": 100, "goals_scored": 10,
                 "assists": 10, "team": 1, "element_type": 4},
                {"id": 2, "first_name": "Bear", "second_name": "Doe", "total_points": 0, "goals_scored": 5,
                 "assists": 0, "team": 1, "element_type": 3},
                {"id": 3, "first_name": "Jane", "second_name": "Doe", "total_points": 10, "goals_scored": 10,
                 "assists": 0, "team": 1, "element_type": 2},
                {"id": 4, "first_name": "Fraser", "second_name": "Doe", "total_points": 50, "goals_scored": 0,
                 "assists": 10, "team": 1, "element_type": 1},
            ],
            "teams": [
                {"id": 1, "name": "Team Doe"},
                {"id": 2, "name": "Team Jane Doe"},
                {"id": 3, "name": "Team John Doe"},
                {"id": 4, "name": "Team Its Doe"},
                {"id": 5, "name": "Team They Doe"}
            ]
        }

    @patch("api.services.requests.get")
    def test_magnificent_7_api_renders(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = self.MOCK_FPL_DATA

        response = self.client.get('/magnificent-7/')
        assert response.status_code == 200

        json_data = response.json()
        assert len(json_data["defenders"]) == 1
        assert json_data["midfielders"][0]['first_name'] == "Bear"
