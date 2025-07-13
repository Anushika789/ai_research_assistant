import pdfplumber
import docx
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_sections(file):
    # Returns a list of (section_title, text) or (None, paragraph)
    if file.type == "application/pdf":
        with pdfplumber.open(file) as pdf:
            sections = []
            for i, page in enumerate(pdf.pages):
                text = page.extract_text() or ""
                paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
                for para in paragraphs:
                    sections.append((f"Page {i+1}", para))
            return sections
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        return [(None, para.text) for para in doc.paragraphs if para.text.strip()]
    elif file.type == "text/plain":
        text = file.read().decode("utf-8")
        return [(None, p) for p in text.split('\n\n') if p.strip()]
    elif file.type in ["image/png", "image/jpeg"]:
        img = Image.open(file)
        text = pytesseract.image_to_string(img)
        return [(None, p) for p in text.split('\n\n') if p.strip()]
    else:
        return []
