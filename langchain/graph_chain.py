from langchain_arangodb import ArangoGraph, ArangoGraphQAChain
from langchain_openai import ChatOpenAI

def get_graph_chain():
    """
    Returns a LangChain QA chain connected to the ArangoDB graph.
    This is used by all demo scripts.
    """
    graph = ArangoGraph(
        db_name="gaming",
        username="root",
        password="root",
        url="http://localhost:8529"
    )

    llm = ChatOpenAI(model="gpt-4o-mini")

    return ArangoGraphQAChain.from_llm(
        llm=llm,
        graph=graph
    )
