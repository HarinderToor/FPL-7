from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import Best7TeamSerializer
from .services import calculate_best_team, TeamMagnificenceCalculatorService


class Magnificence7APIView(APIView):
    def get(self, request):
        best_team = calculate_best_team()
        serializer = Best7TeamSerializer(best_team)
        return Response(serializer.data)

class TeamsMagnificence7APIView(APIView):
    def get(self, request, team_name):
        team_data = TeamMagnificenceCalculatorService.calculate_team_magnificence()
        result = TeamMagnificenceCalculatorService.get_team_top_players(team_data, team_name)

        if result is None:
            return Response({"error": "Team name not found"})
        return Response(result)
