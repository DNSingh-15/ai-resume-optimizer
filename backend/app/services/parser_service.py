import pdfplumber
from docx import Document


def parse_pdf(file):

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:
            content = page.extract_text()

            if content:
                text += content

    return text


def parse_docx(file):

    document = Document(file)

    text = ""

    for para in document.paragraphs:
        text += para.text + "\n"

    return text