import os
from openai import OpenAI

client = None


def get_client():

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return None

    return OpenAI(api_key=api_key)


def analyze_resume(resume_text, job_description):

    client = get_client()

    if not client:
        return {
            "success": False,
            "openai_key_valid": False,
            "message": "OpenAI API key is missing or invalid"
        }

    prompt = f"""
You are an ATS resume analyzer.

Resume:
{resume_text}

Job Description:
{job_description}

Return JSON with:
- ats_score (0-100)
- missing_keywords
- improvements
- optimized_resume
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        content = response.choices[0].message.content

        return {
            "success": True,
            "openai_key_valid": True,
            "data": content
        }

    except Exception as e:

        return {
            "success": False,
            "openai_key_valid": False,
            "message": str(e)
        }