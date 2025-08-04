import os
import PyPDF2

PDF_FOLDER = os.path.join(os.path.dirname(__file__), "..", "Input-files_pdfs")

def extract_text_from_pdf(filename, from_full_path=False):
    if from_full_path:
        full_path = filename
    else:
        full_path = os.path.join(PDF_FOLDER, filename)

    reader = PyPDF2.PdfReader(full_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    return full_text
