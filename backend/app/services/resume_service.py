from app.ai.guardrails.input_guardrail import validate_input
from app.ai.agents.keyword_agent import extract_keywords
from app.ai.scoring.ats_scoring import compute_ats_score
from app.ai.agents.optimization_agent import optimize_resume
from app.ai.guardrails.output_guardrail import validate_output

def analyze_resume(resume_text, job_description):

    validate_input(resume_text, job_description)

    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(job_description)

    ats_score = compute_ats_score(resume_keywords, jd_keywords)

    ai_response = optimize_resume(resume_text, job_description)

    validated = validate_output(ai_response)

    validated["ats_score"] = ats_score

    return validated