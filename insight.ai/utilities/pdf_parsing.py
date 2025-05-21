import os
import pdfplumber
from dotenv import load_dotenv
load_dotenv()


def extract_text_from_pdf():
    """
    Extracts text from a PDF file using pdfplumber.
        
    Returns:
        str: The extracted text from the PDF.
    """
    file_path = os.getenv("PDF_FILE_PATH")
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


print(extract_text_from_pdf())



