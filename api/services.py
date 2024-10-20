from collections import defaultdict

import requests
from rest_framework.exceptions import APIException

FPL_API_URL = "https://cors-proxy-90954623675.europe-west1.run.app/"
GOALKEEPER = 1
DEFENDER = 2
MIDFIELDER = 3
FORWARD = 4

def calculate_magnificence(players):
    return players['goals_scored'] + players['assists']

def calculate_best_team():
    """
    Calculate the best 7 in any team:
    Find all players by position
    Order by "magnificence" descending
    Build a team in a "1-2-2-2" formation
    """
    try:
        response = requests.get(FPL_API_URL)
        response.raise_for_status()
        fpl_data = response.json()

        players = fpl_data['elements']
        goalkeepers = [player for player in players if player['element_type'] == GOALKEEPER]
        defenders = [player for player in players if player['element_type'] == DEFENDER]
        midfielders = [player for player in players if player['element_type'] == MIDFIELDER]
        forwards = [player for player in players if player['element_type'] == FORWARD]

        goalkeepers = sorted(goalkeepers, key=calculate_magnificence, reverse=True)
        defenders = sorted(defenders, key=calculate_magnificence, reverse=True)
        midfielders = sorted(midfielders, key=calculate_magnificence, reverse=True)
        forwards = sorted(forwards, key=calculate_magnificence, reverse=True)

        return {
            'goalkeeper': goalkeepers[0],
            'defenders': defenders[:2],
            'midfielders': midfielders[:2],
            'forwards': forwards[:2]
        }

    except requests.RequestException:
        raise APIException("Error fetching data from the API, try again later.")

class TeamMagnificenceCalculatorService:

    def calculate_team_magnificence():
        team_data = defaultdict(lambda: {'players': []})
        try:
            response = requests.get(FPL_API_URL)
            response.raise_for_status()
            fpl_data = response.json()

            for player in fpl_data['elements']:
                team_id = player['team']
                team_name = next(team['name'].lower() for team in fpl_data['teams'] if team['id'] == team_id)
                player_name = f"{player['first_name']} {player['second_name']}"
                magnificence = player['goals_scored'] + player['assists']

                team_data[team_name]['players'].append({
                    'name': player_name,
                    'magnificence': magnificence
                })
            return team_data
        except requests.RequestException:
            raise APIException("Error fetching data from the API, try again later.")


    def get_team_top_players(team_data, team_name):
        number_of_players = 7
        if team_name not in team_data:
            return None
        team_info = team_data[team_name]
        players = sorted(team_info['players'], key=lambda player: player['magnificence'], reverse=True)[:number_of_players]

        return {
            'name': team_name,
            'players': players
        }
