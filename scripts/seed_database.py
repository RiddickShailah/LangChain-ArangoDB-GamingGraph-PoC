from arango import ArangoClient
import json

# Connect to ArangoDB
client = ArangoClient(hosts="http://localhost:8529")
db = client.db("gaming", username="root", password="root")

# Document collections
collections = [
    "players", "devices", "games", "tournaments",
    "items", "transactions", "rewards", "player_vectors"
]

# Create document collections if missing
for col in collections:
    if not db.has_collection(col):
        db.create_collection(col)

# Edge collections
edge_collections = [
    "played_in", "traded_with", "logged_in_from",
    "won_in", "referred_by"
]

# Create edge collections if missing
for col in edge_collections:
    if not db.has_collection(col):
        db.create_collection(col, edge=True)

# Load documents
for col in collections:
    with open(f"../data/{col}.json") as f:
        docs = json.load(f)
        db.collection(col).import_bulk(docs)

# Load edges
for col in edge_collections:
    with open(f"../data/edges/{col}.json") as f:
        edges = json.load(f)
        db.collection(col).import_bulk(edges)

print("Database seeded successfully!")
