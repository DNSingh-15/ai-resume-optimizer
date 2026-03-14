from pydantic import BaseModel

class ResumeResponse(BaseModel):
    ats_score: int
    missing_keywords: list
    improvements: str
    improved_resume: str