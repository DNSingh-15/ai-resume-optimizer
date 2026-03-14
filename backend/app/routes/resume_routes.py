from fastapi import APIRouter, UploadFile, File, Form
import pdfplumber
import docx
import io

from app.services.resume_service import analyze_resume

router = APIRouter()

@router.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    file_bytes = await resume.read()
    resume_text = ""

    # PDF parsing
    if resume.filename.endswith(".pdf"):

        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            resume_text = "\n".join(page.extract_text() or "" for page in pdf.pages)

    # DOCX parsing
    elif resume.filename.endswith(".docx"):

        doc = docx.Document(io.BytesIO(file_bytes))
        resume_text = "\n".join([p.text for p in doc.paragraphs])

    # TXT fallback
    else:
        resume_text = file_bytes.decode("utf-8", errors="ignore")

    result = analyze_resume(resume_text, job_description)

    return {
        "success": True,
        "data": result
    }