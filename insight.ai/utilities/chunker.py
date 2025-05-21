from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_text(text):
    """
    Splits the input text into smaller chunks using RecursiveCharacterTextSplitter.
    
    Args:
        text (str): The input text to be split.
        
    Returns:
        list: A list of text chunks.
    """
    # Initialize the RecursiveCharacterTextSplitter with custom parameters


    recursive_splitter = RecursiveCharacterTextSplitter(
                    separators=["\n\n", "\n", r"(?<=[.?!])\s+"],                                   
                    keep_separator=False, is_separator_regex=True,
                    chunk_size=30, chunk_overlap=0)


    chunks = recursive_splitter.split_text(text)
    
    
    return chunks