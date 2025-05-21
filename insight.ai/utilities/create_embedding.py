from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")
embeddings = CohereEmbeddings(
    model="embed-english-v3.0",
    cohere_api_key=cohere_api_key
)

    
def create_cohere_embeddings(text_chunks):
    """
    Creates a CohereEmbeddings object using the specified model and API key.
    
    Returns:
        CohereEmbeddings: An instance of the CohereEmbeddings class.
    """
    # Initialize the CohereEmbeddings with the specified model and API key


    embedded_texts = embeddings.embed_documents(text_chunks)
    
    return embedded_texts
