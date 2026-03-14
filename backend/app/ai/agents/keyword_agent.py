import re

def extract_keywords(text):

    words = re.findall(r"\b[A-Za-z]+\b", text.lower())

    keywords = set(words)

    return list(keywords)