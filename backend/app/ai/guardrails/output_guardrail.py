import json

def validate_output(output):

    try:
        data = json.loads(output)
    except:
        raise ValueError("Invalid JSON from LLM")

    required = ["missing_keywords", "improvements", "optimized_resume"]

    for key in required:
        if key not in data:
            raise ValueError("Invalid response structure")

    return data