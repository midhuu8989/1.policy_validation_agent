import re

# Extract important numbers and keywords
def extract_clauses(policies):

    extracted = []

    for i, row in policies.iterrows():

        text = row["policy_text"]

        # Extract percentage values
        percentages = re.findall(r'\d+%', text)

        # Identify keywords
        keywords = []

        if "attendance" in text.lower():
            keywords.append("attendance")

        if "exam" in text.lower():
            keywords.append("exam")

        if "failure" in text.lower():
            keywords.append("failure")

        extracted.append({
            "policy": text,
            "percentages": percentages,
            "keywords": keywords
        })

    return extracted