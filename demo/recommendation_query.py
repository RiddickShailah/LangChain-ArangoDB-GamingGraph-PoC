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
Recommend items to player p1 based on players
with similar transaction histories or embeddings.
"""

response = qa.run(query)

print("\n=== RECOMMENDATION QUERY ===")
print(query)
print("\n=== Response ===")
print(response)
