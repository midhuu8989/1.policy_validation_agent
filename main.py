from retrieval.retriever import load_policies, search_policies
from extractor.clause_extractor import extract_clauses
from validator.validator import validate_policies
from report.report_generator import generate_report

# Load data
data = load_policies("data/policies.csv")

# Query
query = "attendance"

results = search_policies(data, query)

print("\n=== SEARCH RESULTS ===\n")
print(results["policy_text"])

# Extract clauses
extracted = extract_clauses(results)

print("\n=== EXTRACTED CLAUSES ===\n")
for item in extracted:
    print(item)

# Validate
validation = validate_policies(extracted)

print("\n=== VALIDATION RESULTS ===\n")
for v in validation:
    print(v)
    report = generate_report(validation)

print(report)