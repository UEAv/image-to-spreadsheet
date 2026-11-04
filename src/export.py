import pandas as pd
import os

def export_records(records, output_dir="outputs", filename="extracted_portraits"):
    """
    Converts a list of record dictionaries into formatted CSV and Excel files.
    """
    os.makedirs(output_dir, exist_ok=True)
    df = pd.DataFrame(records)
    
    csv_path = os.path.join(output_dir, f"{filename}.csv")
    excel_path = os.path.join(output_dir, f"{filename}.xlsx")
    
    # Export to CSV
    df.to_csv(csv_path, index=False)
    
    # Export to Excel with formatting
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Records')
        worksheet = writer.sheets['Records']
        
        # Format column widths based on data length
        for i, col in enumerate(df.columns):
            max_len = max(df[col].astype(str).map(len).max(), len(col)) + 4
            column_letter = worksheet.cell(row=1, column=i+1).column_letter
            worksheet.column_dimensions[column_letter].width = max_len
        
        # Freeze the header row and add filters
        worksheet.freeze_panes = 'A2'
        worksheet.auto_filter.ref = worksheet.dimensions

    print(f"✅ Successfully exported {len(records)} records.")
    return csv_path, excel_path

if __name__ == "__main__":
    # Quick test
    mock_records = [
        {"S/N": 1, "Name": "Jordan Miller", "Age Range": "Unknown"},
        {"S/N": 2, "Name": "Emily Johnson", "Age Range": "Unknown"}
    ]
    export_records(mock_records)