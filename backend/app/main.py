from fastapi import FastAPI, Query
from app.services.api_football import (
    search_teams,
    get_standings,
    get_live_fixtures,
    get_fixtures_by_date,
)

app = FastAPI(title="Pulse API")

@app.get("/")
def root():
    return {"message": "Pulse API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/teams/search")
def teams_search(name: str = Query(..., min_length=2)):
    return search_teams(name)

@app.get("/standings")
def standings(league: int, season: int):
    return get_standings(league=league, season=season)

@app.get("/live-fixtures")
def live_fixtures():
    return get_live_fixtures()

@app.get("/fixtures/by-date")
def fixtures_by_date(date: str):
    return get_fixtures_by_date(date=date)