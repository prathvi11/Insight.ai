from utilities.pdf_parsing import extract_text_from_pdf
from utilities.chunker import split_text
from utilities.create_embedding import create_cohere_embeddings
from utilities.store_in_vectorDB import upload_documents
from utilities.llm import answer_queries



extract_text = extract_text_from_pdf()
if len(extract_text) > 0:
    print("Text is extracted successfully!")
else:  
    print("Text extraction failed!")
    
text_chunks = split_text(extract_text)
if len(text_chunks) > 0:
    print("Text is chunked successfully!") 
else:
    print("Text chunking failed!")
    
text_embedd = create_cohere_embeddings(text_chunks)
if len(text_embedd) > 0:
    print("Text is embedded successfully!") 
else:   
    print("Text embedding failed!")
    
upload_documents(text_chunks)

while True:
    question = input("Ask a question: ")
    if question.lower() == "exit":
        break
    answer = answer_queries(question)
    print(answer)
    


    

    
