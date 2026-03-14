def compute_ats_score(resume_keywords, jd_keywords):

    matched = set(resume_keywords) & set(jd_keywords)

    score = (len(matched) / len(jd_keywords)) * 100

    return round(score)