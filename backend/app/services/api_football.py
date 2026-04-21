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

def format_live_fixtures(data: dict):
    fixtures = []

    for item in data.get("response", []):
        fixtures.append({
            "fixture_id": item["fixture"]["id"],
            "league": item["league"]["name"],
            "home_team": item["teams"]["home"]["name"],
            "away_team": item["teams"]["away"]["name"],
            "home_logo": item["teams"]["home"]["logo"],
            "away_logo": item["teams"]["away"]["logo"],
            "home_score": item["goals"]["home"],
            "away_score": item["goals"]["away"],
            "status": item["fixture"]["status"]["short"],
            "elapsed": item["fixture"]["status"]["elapsed"],
        })

    return fixtures


def format_standings(data: dict):
    standings_table = []

    response = data.get("response", [])
    if not response:
        return standings_table

    table = response[0]["league"]["standings"][0]

    for row in table:
        standings_table.append({
            "rank": row["rank"],
            "team_name": row["team"]["name"],
            "team_logo": row["team"]["logo"],
            "points": row["points"],
            "played": row["all"]["played"],
            "won": row["all"]["win"],
            "draw": row["all"]["draw"],
            "lost": row["all"]["lose"],
            "goal_difference": row["goalsDiff"],
            "form": row["form"],
        })

    return standings_table


def format_fixtures_by_date(data: dict):
    fixtures = []

    for item in data.get("response", []):
        fixtures.append({
            "fixture_id": item["fixture"]["id"],
            "date": item["fixture"]["date"],
            "league": item["league"]["name"],
            "home_team": item["teams"]["home"]["name"],
            "away_team": item["teams"]["away"]["name"],
            "home_logo": item["teams"]["home"]["logo"],
            "away_logo": item["teams"]["away"]["logo"],
            "home_score": item["goals"]["home"],
            "away_score": item["goals"]["away"],
            "status": item["fixture"]["status"]["short"],
        })

    return fixtures