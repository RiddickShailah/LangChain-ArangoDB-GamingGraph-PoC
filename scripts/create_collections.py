from arango import ArangoClient

client = ArangoClient(hosts="http://localhost:8529")
db = client.db("gaming", username="root", password="root")

collections = [
    "players", "devices", "games", "tournaments",
    "items", "transactions", "rewards", "player_vectors"
]

for col in collections:
    if not db.has_collection(col):
        db.create_collection(col)

edge_collections = [
    "played_in", "traded_with", "logged_in_from",
    "won_in", "referred_by"
]

for col in edge_collections:
    if not db.has_collection(col):
        db.create_collection(col, edge=True)

print("Collections created.")
