from retrieval.retriever import load_policies, search_policies
from extractor.clause_extractor import extract_clauses
from validator.validator import validate_policies
from report.report_generator import generate_report


def main():
    # Load data
    try:
        data = load_policies("data/policies.csv")
    except Exception as e:
        print(f"Error loading policies: {e}")
        return

    # Query
    query = "attendance"

    # Search
    try:
        results = search_policies(data, query)
    except Exception as e:
        print(f"Error during search: {e}")
        return

    print("\n=== SEARCH RESULTS ===\n")

    # Handle empty results
    if not results:
        print("No results found.")
        return

    # Print results safely
    if isinstance(results, dict) and "policy_text" in results:
        print(results["policy_text"])
    else:
        print(results)

    # Extract clauses
    try:
        extracted = extract_clauses(results)
    except Exception as e:
        print(f"Error extracting clauses: {e}")
        return

    print("\n=== EXTRACTED CLAUSES ===\n")
    if not extracted:
        print("No clauses extracted.")
        return

    for item in extracted:
        print(item)

    # Validate
    try:
        validation = validate_policies(extracted)
    except Exception as e:
        print(f"Error validating policies: {e}")
        return

    print("\n=== VALIDATION RESULTS ===\n")
    if not validation:
        print("No validation results.")
        return

    for v in validation:
        print(v)

    # Generate report (FIXED: outside loop)
    try:
        report = generate_report(validation)
    except Exception as e:
        print(f"Error generating report: {e}")
        return

    print("\n=== FINAL REPORT ===\n")
    print(report)


if __name__ == "__main__":
    main()
