from langchain_arangodb import ArangoGraph, ArangoGraphQAChain
from langchain_openai import ChatOpenAI

# Connect to ArangoDB
graph = ArangoGraph(
    db_name="gaming",
    username="root",
    password="root",
    url="http://localhost:8529"
)

# LLM for natural language → AQL
llm = ChatOpenAI(model="gpt-4o-mini")

qa = ArangoGraphQAChain.from_llm(llm=llm, graph=graph)

# Basic test query
query = "List all players who logged in from the same device as player p1."
response = qa.run(query)

print("\n=== Natural Language Query ===")
print(query)
print("\n=== Response ===")
print(response)
