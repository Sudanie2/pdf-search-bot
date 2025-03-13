import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """PDFからテキストを抽出"""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text
