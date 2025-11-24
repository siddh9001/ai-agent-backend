from app.core.models import vector_store

def search_similar_text(embedding: list[float], k: int = 2):
    try:
        results = vector_store.similarity_search_by_vector(embedding=embedding, k=k)
        return [{"page_content": doc.page_content, "metadata": doc.metadata} for doc in results]
    except Exception as e:
        print(f"Search error: {str(e)}")
        return []
