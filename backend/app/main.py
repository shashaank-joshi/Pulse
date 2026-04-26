from fastapi import FastAPI, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.database import SessionLocal, engine, Base
from app.models.tracked_team import TrackedTeam as TrackedTeamModel
from app.services.api_football import (
    search_teams,
    get_live_fixtures,
    get_fixtures_by_date,
    format_live_fixtures,
    format_fixtures_by_date,
    get_date_strings,
    get_past_date_strings,
)

Base.metadata.create_all(bind=engine)

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


class TrackedTeam(BaseModel):
    team_id: int
    team_name: str
    team_logo: str
    country: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
def get_tracked_teams(db: Session = Depends(get_db)):
    teams = db.query(TrackedTeamModel).all()

    return {
        "teams": [
            {
                "team_id": team.team_id,
                "team_name": team.team_name,
                "team_logo": team.team_logo,
                "country": team.country,
            }
            for team in teams
        ]
    }


@app.post("/pulse/tracked-teams")
def add_tracked_team(team: TrackedTeam, db: Session = Depends(get_db)):
    existing_team = db.query(TrackedTeamModel).filter(
        TrackedTeamModel.team_id == team.team_id
    ).first()

    if existing_team:
        return {"message": "Team already tracked"}

    new_team = TrackedTeamModel(
        team_id=team.team_id,
        team_name=team.team_name,
        team_logo=team.team_logo,
        country=team.country,
    )

    db.add(new_team)
    db.commit()
    db.refresh(new_team)

    return {"message": "Team tracked successfully"}


@app.get("/pulse/live")
def pulse_live():
    raw_data = get_live_fixtures()
    return {"matches": format_live_fixtures(raw_data)}


@app.get("/pulse/fixtures/date")
def pulse_fixtures_by_date(date: str):
    raw_data = get_fixtures_by_date(date=date)
    return {"matches": format_fixtures_by_date(raw_data)}


@app.get("/pulse/tracked-teams/upcoming")
def get_upcoming_tracked_team_matches(db: Session = Depends(get_db)):
    teams = db.query(TrackedTeamModel).all()

    if not teams:
        return {"matches": []}

    tracked_team_ids = {team.team_id for team in teams}
    upcoming_matches = []
    seen_fixture_ids = set()

    for date in get_date_strings(7):
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


@app.get("/pulse/tracked-teams/recent")
def get_recent_tracked_team_matches(db: Session = Depends(get_db)):
    teams = db.query(TrackedTeamModel).all()

    if not teams:
        return {"matches": []}

    tracked_team_ids = {team.team_id for team in teams}
    recent_matches = []
    seen_fixture_ids = set()

    for date in get_past_date_strings(7):
        raw_data = get_fixtures_by_date(date)
        formatted_matches = format_fixtures_by_date(raw_data)

        for raw_item, formatted_item in zip(raw_data.get("response", []), formatted_matches):
            home_team_id = raw_item["teams"]["home"]["id"]
            away_team_id = raw_item["teams"]["away"]["id"]
            status = raw_item["fixture"]["status"]["short"]

            if home_team_id in tracked_team_ids or away_team_id in tracked_team_ids:
                if status in ["FT", "AET", "PEN"]:
                    fixture_id = formatted_item["fixture_id"]

                    if fixture_id not in seen_fixture_ids:
                        seen_fixture_ids.add(fixture_id)
                        recent_matches.append(formatted_item)

    recent_matches.sort(key=lambda x: x["date"], reverse=True)
    return {"matches": recent_matches}