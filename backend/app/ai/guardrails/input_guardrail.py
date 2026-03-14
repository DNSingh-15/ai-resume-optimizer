def validate_input(resume_text, job_description):

    if not resume_text:
        raise ValueError("Resume text is empty")

    if len(resume_text) < 200:
        raise ValueError("Resume too short")

    if len(resume_text) > 15000:
        raise ValueError("Resume too large")

    if not job_description:
        raise ValueError("Job description required")

    return True