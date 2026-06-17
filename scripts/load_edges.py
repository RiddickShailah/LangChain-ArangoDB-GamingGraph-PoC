from arango import ArangoClient
import json

client = ArangoClient(hosts="http://localhost:8529")
db = client.db("gaming", username="root", password="root")

edge_collections = [
    "played_in", "traded_with", "logged_in_from",
    "won_in", "referred_by"
]

for col in edge_collections:
    with open(f"../data/edges/{col}.json") as f:
        edges = json.load(f)
        db.collection(col).import_bulk(edges)

print("Edges loaded.")
