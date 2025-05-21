from utilities.store_in_vectorDB import vector_store

def search_documents(query, k=2):
    """
    Searches for documents in the vector store using a query.
    
    Args:
        query (str): The query string to search for.
        k (int): The number of top results to return.
        
    Returns:
        list: A list of the top k documents matching the query.
    """
    
    results = vector_store.similarity_search(query, k=k)
    
    return results

# results = vector_store.similarity_search(
#     "LangChain provides abstractions to make working with LLMs easy",
#     k=2,
#     filter={"source": "tweet"},
# )
# for res in results:
#     print(f"* {res.page_content} [{res.metadata}]")