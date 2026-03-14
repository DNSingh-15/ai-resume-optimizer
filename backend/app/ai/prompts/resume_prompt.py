def resume_prompt(resume, jd):

    return f"""
You are an ATS resume optimization expert.

Resume:
{resume}

Job Description:
{jd}

Return strictly JSON:

{{
"missing_keywords": [],
"improvements": [],
"optimized_resume": {{}}
}}
"""