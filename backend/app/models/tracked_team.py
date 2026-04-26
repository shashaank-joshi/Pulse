from sqlalchemy import Column, Integer, String
from app.db.database import Base

class TrackedTeam(Base):
    __tablename__ = "tracked_teams"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, unique=True, nullable=False)
    team_name = Column(String, nullable=False)
    team_logo = Column(String, nullable=False)
    country = Column(String, nullable=False)