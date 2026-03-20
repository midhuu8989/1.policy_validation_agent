def generate_report(validation_results):

    report = []

    report.append("\n===== POLICY VALIDATION REPORT =====\n")

    aligned = 0
    partial = 0
    missing = 0

    for item in validation_results:

        report.append(f"Policy: {item['policy']}")
        report.append(f"Status: {item['status']}\n")

        if item["status"] == "Aligned":
            aligned += 1
        elif item["status"] == "Partial":
            partial += 1
        else:
            missing += 1

    # Confidence logic
    total = len(validation_results)

    if aligned == total:
        confidence = "High"
    elif aligned > 0:
        confidence = "Medium"
    else:
        confidence = "Low"

    report.append("Summary:")
    report.append(f"Aligned: {aligned}")
    report.append(f"Partial: {partial}")
    report.append(f"Missing: {missing}")
    report.append(f"Confidence Level: {confidence}")

    return "\n".join(report)