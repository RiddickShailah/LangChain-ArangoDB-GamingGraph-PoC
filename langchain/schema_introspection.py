from langchain_arangodb import ArangoGraph

def get_schema():
    """
    Returns the ArangoDB graph schema.
    Useful for debugging and verifying that
    collections + edges are correctly loaded.
    """
    graph = ArangoGraph(
        db_name="gaming",
        username="root",
        password="root",
        url="http://localhost:8529"
    )
    return graph.schema
