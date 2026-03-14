from fastapi import APIRouter, UploadFile, File, Form
from app.services.parser_service import parse_pdf, parse_docx
from app.services.ai_service import analyze_resume

router = APIRouter()


@router.post("/analyze")
async def analyze_resume_api(
        file: UploadFile = File(...),
        job_description: str = Form(...)
):

    try:

        filename = file.filename

        if filename.endswith(".pdf"):

            resume_text = parse_pdf(file.file)

        elif filename.endswith(".docx"):

            resume_text = parse_docx(file.file)

        else:

            return {
                "success": False,
                "message": "Unsupported file format. Use PDF or DOCX"
            }

        ai_result = analyze_resume(resume_text, job_description)

        return ai_result

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }