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
Show all players within 3 hops of player p1
who share a device or traded items with them.
"""

response = qa.run(query)

print("\n=== FRAUD DETECTION QUERY ===")
print(query)
print("\n=== Response ===")
print(response)
