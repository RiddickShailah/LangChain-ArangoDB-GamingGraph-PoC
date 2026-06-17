from langchain_arangodb import ArangoGraph
from langchain_openai import ChatOpenAI

graph = ArangoGraph(
    url="http://localhost:8529",
    username="root",
    password="root",
    database="gaming"
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
