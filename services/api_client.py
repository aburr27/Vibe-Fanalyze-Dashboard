# This file handles ALL communication with your FastAPI backend

import requests  # allows us to send HTTP requests

# Base URL of your FastAPI backend
BASE_URL = "http://127.0.0.1:8000"


def get_teams():
    """
    Fetch all teams from the API
    """
    # Send GET request to backend
    response = requests.get(f"{BASE_URL}/teams/")

    # Convert response JSON into Python list/dict
    return response.json()


def get_players():
    """
    Fetch all players from the API
    """
    response = requests.get(f"{BASE_URL}/players/")
    return response.json()


def get_games():
    """
    Fetch all games from the API
    """
    response = requests.get(f"{BASE_URL}/games/")
    return response.json()
