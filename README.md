# Gaming & Gambling Knowledge Graph Assistant (LangChain + ArangoDB)

This Proof of Concept demonstrates how ArangoDB’s multi-model engine (graph + document + vector)
combined with LangChain enables natural-language querying over complex gaming/gambling ecosystems.

## Features
- Multi-hop fraud & collusion detection
- Tournament/IP subnet compliance analysis
- Vector-based item recommendations
- Natural language → AQL using ArangoGraphQAChain
- Unified graph + document + vector architecture

## Dataset
Synthetic dataset includes:
- 10 players
- 6 devices
- 4 games
- 3 tournaments
- 6 items
- 12 transactions
- 10 player vectors
- 5 edge types (played_in, traded_with, logged_in_from, won_in, referred_by)

## Running the Demo
1. Start ArangoDB locally:
docker run -e ARANGO_ROOT_PASSWORD=password -p 8529:8529 arangodb

2. Install dependencies:
pip install -r requirements.txt

3. Seed the database:
python seed_database.py

4. Run the LangChain demo:
python demo.py


## Architecture
- ArangoGraph for schema introspection
- ArangoGraphQAChain for NL → AQL
- ArangoVector for semantic similarity
