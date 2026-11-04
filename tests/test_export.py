import pandas as pd
import os

print("--- Testing Spreadsheet Generation ---")

# Mock data simulating what our pipeline will eventually produce
# Note: 'Age Range' is set to 'Unknown' until we build the AI model in Stage 9
records = [
    {"S/N": 1, "Name": "Jordan Miller", "Age Range": "Unknown"},
    {"S/N": 2, "Name": "Emily Johnson", "Age Range": "Unknown"},
    {"S/N": 3, "Name": "Roger Blake", "Age Range": "Unknown"}
]

# Convert the dictionary list into a Pandas DataFrame
df = pd.DataFrame(records)
print("\nGenerated DataFrame:")
print(df.to_string(index=False))
print("-" * 30)

os.makedirs("outputs", exist_ok=True)

# Export to CSV
csv_path = "outputs/test_records.csv"
df.to_csv(csv_path, index=False)
print(f"✅ Saved CSV file to {csv_path}")

# Export to Excel
excel_path = "outputs/test_records.xlsx"
df.to_excel(excel_path, index=False)
print(f"✅ Saved Excel file to {excel_path}")