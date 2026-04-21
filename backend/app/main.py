from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.services.api_football import (
    search_teams,
    get_standings,
    get_live_fixtures,
    get_fixtures_by_date,
    format_live_fixtures,
    format_standings,
    format_fixtures_by_date,
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
