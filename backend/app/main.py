from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.services.api_football import (
    search_teams,
    get_standings,
    get_live_fixtures,
    get_fixtures_by_date,
    format_live_fixtures,
    format_standings,
    format_fixtures_by_date,
    get_date_strings,
)

app = FastAPI(title="Pulse API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tracked_teams = []


class TrackedTeam(BaseModel):
    team_id: int
    team_name: str
    team_logo: str
    country: str


@app.get("/")
def root():
    return {"message": "Pulse API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/pulse/teams/search")
def pulse_teams_search(name: str = Query(..., min_length=2)):
    raw_data = search_teams(name)

    teams = []
    for item in raw_data.get("response", []):
        teams.append({
            "team_id": item["team"]["id"],
            "team_name": item["team"]["name"],
            "team_logo": item["team"]["logo"],
            "country": item["team"]["country"],
        })

    return {"teams": teams}


@app.get("/pulse/tracked-teams")
def get_tracked_teams():
    return {"teams": tracked_teams}


@app.post("/pulse/tracked-teams")
def add_tracked_team(team: TrackedTeam):
    for existing_team in tracked_teams:
        if existing_team["team_id"] == team.team_id:
            return {"message": "Team already tracked", "teams": tracked_teams}

    tracked_teams.append(team.dict())
    return {"message": "Team tracked successfully", "teams": tracked_teams}


@app.get("/pulse/live")
def pulse_live():
    raw_data = get_live_fixtures()
    return {"matches": format_live_fixtures(raw_data)}


@app.get("/pulse/standings")
def pulse_standings(league: int, season: int):
    raw_data = get_standings(league=league, season=season)
    return {"table": format_standings(raw_data)}


@app.get("/pulse/fixtures/date")
def pulse_fixtures_by_date(date: str):
    raw_data = get_fixtures_by_date(date=date)
    return {"matches": format_fixtures_by_date(raw_data)}

@app.get("/pulse/tracked-teams/upcoming")
def get_upcoming_tracked_team_matches():
    if not tracked_teams:
        return {"matches": []}

    tracked_team_ids = {team["team_id"] for team in tracked_teams}
    upcoming_matches = []
    seen_fixture_ids = set()

    for date in get_date_strings(4):
        raw_data = get_fixtures_by_date(date)
        formatted_matches = format_fixtures_by_date(raw_data)

        for raw_item, formatted_item in zip(raw_data.get("response", []), formatted_matches):
            home_team_id = raw_item["teams"]["home"]["id"]
            away_team_id = raw_item["teams"]["away"]["id"]

            if home_team_id in tracked_team_ids or away_team_id in tracked_team_ids:
                fixture_id = formatted_item["fixture_id"]

                if fixture_id not in seen_fixture_ids:
                    seen_fixture_ids.add(fixture_id)
                    upcoming_matches.append(formatted_item)

    return {"matches": upcoming_matches}