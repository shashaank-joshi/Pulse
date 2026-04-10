# Pulse Architecture (V1)

## Frontend
Next.js app for dashboard, favorites, notes, and search.

## Backend
FastAPI service exposes APIs for:
- favorites
- sports updates
- notes
- summaries
- search

## Database
PostgreSQL stores structured app data such as favorites, sports updates, notes, and summaries.

## Data Ingestion
A simple ingestion script fetches football data from an external API and stores relevant updates in PostgreSQL.

## AI Layer
A summary service takes recent sports updates and/or notes as input and generates a concise summary.

## Cloud
AWS will be used gradually, starting with low-cost services such as S3 for raw payload storage and scheduled jobs later if needed.