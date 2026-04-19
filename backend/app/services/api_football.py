import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_FOOTBALL_KEY")
BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    "x-apisports-key": API_KEY
}

def search_teams(name: str):
    response = requests.get(
        f"{BASE_URL}/teams",
        headers=HEADERS,
        params={"search": name},
        timeout=15,
    )
    response.raise_for_status()
    return response.json()

def get_team_fixtures(team_id: int, season: int, last: int = None, next_count: int = None):
    params = {
        "team": team_id,
        "season": season,
    }

    if last is not None:
        params["last"] = last

    if next_count is not None:
        params["next"] = next_count

    response = requests.get(
        f"{BASE_URL}/fixtures",
        headers=HEADERS,
        params=params,
        timeout=15,
    )
    response.raise_for_status()
    return response.json()

def get_standings(league: int, season: int):
    response = requests.get(
        f"{BASE_URL}/standings",
        headers=HEADERS,
        params={"league": league, "season": season},
        timeout=15,
    )
    response.raise_for_status()
    return response.json()

def get_live_fixtures():
    response = requests.get(
        f"{BASE_URL}/fixtures",
        headers=HEADERS,
        params={"live": "all"},
        timeout=15,
    )
    response.raise_for_status()
    return response.json()

def get_fixtures_by_date(date: str):
    response = requests.get(
        f"{BASE_URL}/fixtures",
        headers=HEADERS,
        params={"date": date},
        timeout=15,
    )
    response.raise_for_status()
    return response.json()