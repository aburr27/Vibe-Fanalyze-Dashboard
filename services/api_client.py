# This file handles ALL communication with your FastAPI backend

import requests  # allows us to send HTTP requests

# Base URL of your FastAPI backend
BASE_URL = "http://127.0.0.1:8000"

# Store token globally (simple approach for now)
TOKEN = None

def set_token(token: str):
    """
    Save JWT token after login
    """
    global TOKEN
    TOKEN = token


def get_headers():
    """
    Add Authorization header if logged in
    """
    if TOKEN:
        return {"Authorization": f"Bearer {TOKEN}"}
    return {}


def login(email: str, password: str):
    """
    Send login request to API
    """
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={"email": email, "password": password}
    )

    return response.json()

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
