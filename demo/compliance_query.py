from langchain_arangodb import ArangoGraph, ArangoGraphQAChain
from langchain_openai import ChatOpenAI

graph = ArangoGraph(
    db_name="gaming",
    username="root",
    password="root",
    url="http://localhost:8529"
)

llm = ChatOpenAI(model="gpt-4o-mini")

qa = ArangoGraphQAChain.from_llm(llm=llm, graph=graph)

query = """
Which tournaments have the highest concentration
of players from the same IP subnet?
"""

response = qa.run(query)

print("\n=== COMPLIANCE QUERY ===")
print(query)
print("\n=== Response ===")
print(response)
