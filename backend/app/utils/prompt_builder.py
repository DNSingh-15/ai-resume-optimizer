def build_prompt(resume_text, job_description):

    prompt = f"""
You are a professional ATS resume optimizer.

Analyze the following resume and job description.

Resume:
{resume_text}

Job Description:
{job_description}

Return:

ATS Score (0-100)

Missing Keywords

Improved Bullet Points

Optimized Resume Version
"""

    return prompt