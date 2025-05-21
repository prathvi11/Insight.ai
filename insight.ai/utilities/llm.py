from langchain_cohere import ChatCohere
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from utilities.store_in_vectorDB import vector_store
from dotenv import load_dotenv
import os
load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")

llm = ChatCohere(max_tokens=256, temperature=0.75, cohere_api_key=cohere_api_key)


system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

def answer_queries(question):
    """
    Function to answer a question using the RAG chain.
    
    Args:
        question (str): The question to be answered.
        
    Returns:
        str: The answer to the question.
    """
    prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
    )
    
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(vector_store, question_answer_chain)
    results = rag_chain.invoke({"input": question})
    return results
