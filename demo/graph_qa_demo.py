from arango import ArangoClient
from langchain_arangodb import ArangoGraph
from langchain_arangodb import ArangoGraphQAChain
from langchain_groq import ChatGroq
import os

# 1. Connect to ArangoDB
client = ArangoClient(hosts="http://localhost:8529")
db = client.db("gaming", username="root", password="root")

# 2. Initialize ArangoGraph
graph = ArangoGraph(db=db)

# 3. Use Groq LLM (free)
from langchain_groq import ChatGroq

llm = ChatGroq(    model="llama-3.3-70b-versatile",
                   temperature=0,
                   api_key=os.getenv("GROQ_API_KEY"),
)


# 4. Build the QA chain
qa = ArangoGraphQAChain.from_llm(
    graph=graph,
    llm=llm,
    include_schema=True,
    max_depth=3,
    allow_dangerous_requests=True
)

# 5. Run a test query
query = "List all players who logged in from the same device as player p1."
response = qa.invoke(query)

print("\n=== Natural Language Query ===")
print(query)
print("\n=== Response ===")
print(response)



