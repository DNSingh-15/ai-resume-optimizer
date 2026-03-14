from app.ai.llm.openai_client import call_llm
from app.ai.prompts.resume_prompt import resume_prompt

def optimize_resume(resume_text, job_description):

    prompt = resume_prompt(resume_text, job_description)

    return call_llm(prompt)