# Pulse Schema V2

## Overview
Pulse is a personalized sports and culture intelligence platform.  
The V1 schema is centered on sports first, with room to expand into music and broader discovery features.

---

## tracked_teams
Stores teams the user wants to follow.

Fields:
- id
- team_name
- external_api_id
- league_name
- country
- logo_url
- created_at

Purpose:
- powers the personalized sports experience
- links followed teams to matches, summaries, and discovery cards

---

## matches
Stores recent and upcoming matches for tracked teams.

Fields:
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
- venue
- created_at
- updated_at

Purpose:
- supports recent results
- supports upcoming fixtures
- powers homepage sports modules

---

## tracked_artists
Stores artists the user wants to follow.

Fields:
- id
- artist_name
- external_api_id
- genre
- image_url
- created_at

Purpose:
- enables future music discovery features
- keeps music as a secondary but connected product pillar

---

## content_cards
Stores discovery content shown on the homepage.

Fields:
- id
- card_type
- title
- description
- source
- related_entity_type
- related_entity_name
- created_at

Examples:
- sports fact
- music recommendation
- pop culture insight
- trending topic

Purpose:
- powers the discovery section
- supports “interesting now” style experiences
- keeps the product flexible beyond pure sports data

---

## summaries
Stores generated summaries for tracked interests.

Fields:
- id
- entity_type
- entity_name
- summary_type
- summary_text
- source_context
- created_at

Examples:
- weekly team summary
- recent discussion summary
- why-this-matters summary

Purpose:
- supports AI-generated summaries
- gives the product an intelligence layer instead of just raw data

---

## Future Tables (Not in V1 yet)

### players
Could store tracked football players for deeper personalization.

Fields:
- id
- player_name
- external_api_id
- team_name
- nationality
- position
- created_at

### user_preferences
Could store display and recommendation preferences.

Fields:
- id
- favorite_competitions
- favorite_topics
- summary_frequency
- created_at
- updated_at

### game_sessions
Could support mini-games like Guess the Footballer.

Fields:
- id
- game_type
- difficulty
- result
- played_at