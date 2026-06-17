from arango import ArangoClient
from langchain_arangodb import ArangoGraph
from langchain_openai import ChatOpenAI

# 1. Connect to ArangoDB
client = ArangoClient(hosts="http://localhost:8529")
db = client.db("gaming", username="root", password="root")

# 2. Initialize ArangoGraph (NO arguments in your version)
graph = ArangoGraph()

# 3. Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 4. Build the QA chain using the new API
qa = graph.query_llm(
    llm=llm,
    db=db,                 # <-- THIS is where the DB connection goes now
    include_schema=True,
    max_depth=3
)

# 5. Run a test query
query = "List all players who logged in from the same device as player p1."
response = qa.invoke(query)

print("\n=== Natural Language Query ===")
print(query)
print("\n=== Response ===")
print(response)

