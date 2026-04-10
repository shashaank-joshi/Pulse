# Initial Schema Draft

## favorites
- id
- category (team, player, artist, song, genre)
- name
- external_id
- source
- created_at

## sports_updates
- id
- team_name
- competition
- match_date
- opponent
- result
- status
- summary
- raw_payload_url
- created_at

## music_items
- id
- item_type (artist, song, album, genre)
- name
- artist_name
- notes
- source
- created_at

## notes
- id
- title
- content
- category (sports, music, trivia, general)
- tags
- linked_entity
- created_at
- updated_at

## summaries
- id
- title
- summary_type
- input_context
- output_text
- created_at