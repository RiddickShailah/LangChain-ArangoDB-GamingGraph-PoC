from langchain_openai import OpenAIEmbeddings

def embed_text(text: str):
    """
    Generates an embedding vector for a given text.
    Used for similarity search and recommendations.
    """
    embedder = OpenAIEmbeddings(model="text-embedding-3-small")
    return embedder.embed_query(text)
