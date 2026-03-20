import pandas as pd

# Load policy data
def load_policies(file_path):
    data = pd.read_csv(file_path)
    return data

# Simple keyword search
def search_policies(data, query):

    query = query.lower()
    results = []

    for i, row in data.iterrows():

        policy_text = row["policy_text"].lower()

        if query in policy_text:
            results.append(row)

    return pd.DataFrame(results)