
import csv

CSV_PATH = r"C:\Users\rajes\Desktop\Project 1\capture.csv"

def parse_csv():
    results = {"files written": [], "registry mods": [], "network access": []}

    with open(CSV_PATH, newline='', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Get the relevant columns from the row
            path = row.get("Path", "")
            op = row.get("Operation", "")

            # Check if the operation is one of the target actions and append the path to the respective list
            if "WriteFile" in op:
                results["files written"].append(path)
            elif "RegSetValue" in op or "RegCreateKey" in op:
                results["registry mods"].append(path)
            elif "TCP" in op or "UDP" in op:
                results["network access"].append(path)
    
    return results
