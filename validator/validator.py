# Define expected rules (checklist)
EXPECTED_RULES = {
    "attendance": {
        "min_required": 75
    }
}

def validate_policies(extracted_clauses):

    results = []

    for item in extracted_clauses:

        status = "Missing"

        # Check attendance rule
        if "attendance" in item["keywords"]:

            percentages = item["percentages"]

            if percentages:

                value = int(percentages[0].replace("%", ""))

                if value >= EXPECTED_RULES["attendance"]["min_required"]:
                    status = "Aligned"
                else:
                    status = "Partial"

        results.append({
            "policy": item["policy"],
            "status": status
        })

    return results