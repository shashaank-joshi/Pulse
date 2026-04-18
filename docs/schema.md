# Pulse Schema V2

## tracked_teams
- id
- team_name
- external_api_id
- league_name
- country
- created_at

## matches
- id
- external_match_id
- home_team
- away_team
- competition
- match_datetime
- status
- home_score
- away_score
- winner
- created_at
- updated_at

## tracked_artists
- id
- artist_name
- external_api_id
- genre
- created_at

## content_cards
- id
- card_type
- title
- description
- source
- related_entity
- created_at

## summaries
- id
- entity_type
- entity_name
- summary_type
- summary_text
- source_context
- created_at