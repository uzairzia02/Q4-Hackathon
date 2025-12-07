# Data Model for Physical AI Book

This document outlines the data models for the key entities in the Physical AI Book project.

## User

Represents a reader of the book.

- **user_id**: `UUID` (Primary Key)
- **email**: `String` (Unique)
- **profile**: `JSONB`
  - **hardware_tier**: `String` (e.g., 'simulation-first', 'cloud-based', 'edge-deployment')
  - **experience_level**: `String` (e.g., 'beginner', 'intermediate', 'expert')
  - **learning_goals**: `Array<String>`
- **reading_progress**: `JSONB`
  - `{ "chapter_<N>": "completed" }`

## Chapter

A chapter of the book.

- **chapter_id**: `UUID` (Primary Key)
- **week_number**: `Integer` (Unique)
- **title**: `String`
- **content_english**: `Text`
- **content_urdu**: `Text`

## QA_Session

A user's interaction with the RAG chatbot.

- **session_id**: `UUID` (Primary Key)
- **user_id**: `UUID` (Foreign Key to User)
- **question**: `Text`
- **answer**: `Text`
- **context**: `Text`
- **timestamp**: `Timestamp`

## GlossaryTerm

A term in the technical glossary.

- **term_id**: `UUID` (Primary Key)
- **term**: `String` (Unique)
- **definition**: `Text`
