import json
from arango import ArangoClient

# -----------------------------
# 1. Connect to ArangoDB
# -----------------------------
client = ArangoClient(hosts="http://localhost:8529")
db = client.db("gaming", username="root", password="root")

print("\n Starting database seeding...\n")

# -----------------------------
# 2. Collections to load
# -----------------------------
DOCUMENT_COLLECTIONS = [
    "players",
    "devices",
    "games",
    "items",
    "tournaments",
    "transactions",
    "player_vectors",
    "rewards"
]

EDGE_COLLECTIONS = [
    "logged_in_from",
    "played_in",
    "traded_with",
    "won_in",
    "referred_by"
]

# -----------------------------
# 3. Helper: load JSON file
# -----------------------------
def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

# -----------------------------
# 4. Create + truncate collections
# -----------------------------
def ensure_collection(name, edge=False):
    if not db.has_collection(name):
        db.create_collection(name, edge=edge)
        print(f"  ➕ Created collection: {name}")
    else:
        print(f"  ✔ Collection exists: {name}")

    # Always truncate to avoid duplicate key errors
    db.collection(name).truncate()
    print(f"   Truncated: {name}")

# -----------------------------
# 5. Load document collections
# -----------------------------
print(" Loading document collections...\n")

for col in DOCUMENT_COLLECTIONS:
    ensure_collection(col, edge=False)
    docs = load_json(f"data/{col}.json")
    db.collection(col).import_bulk(docs)
    print(f"  Inserted {len(docs)} documents into {col}\n")

# -----------------------------
# 6. Load edge collections
# -----------------------------
print(" Loading edge collections...\n")

for col in EDGE_COLLECTIONS:
    ensure_collection(col, edge=True)
    edges = load_json(f"data/edges/{col}.json")
    db.collection(col).import_bulk(edges)
    print(f"  Inserted {len(edges)} edges into {col}\n")

# -----------------------------
# 7. Done
# -----------------------------
print("\n Database seeding complete! All collections loaded successfully.\n")

