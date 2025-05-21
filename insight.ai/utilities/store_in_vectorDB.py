import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from utilities.create_embedding import embeddings
from uuid import uuid4
from langchain_core.documents import Document


index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))

# Create a FAISS vector store with the specified embedding function and index
vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)


def upload_documents(text_chunks):
    """
    Uploads documents to a FAISS vector store using Cohere embeddings.
    
    Args:
        text_chubnks (list): A list of documents to be uploaded.
        
    Returns:
        None
    """


    uuids = [str(uuid4()) for _ in range(len(text_chunks))]
    documents = [Document(page_content=text) for text in text_chunks]

    vector_store.add_documents(documents=documents, ids=uuids)
    
    print("Documents uploaded successfully.")