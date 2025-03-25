import os
import gzip

# Set the root directory where your month folders are located
# root_dir = r"D:\Work\Full-time\Uptimal\Test case\NYC_311_Data"
# combined_file_path = os.path.join(root_dir, "combined.csv")

# # Flag to know if header has been written
# first_chunk = True

# # Open the combined output file in binary write mode
# with open(combined_file_path, "wb") as fout:
#     # Get all subdirectories sorted (assuming folder names like 2024_01, 2024_02, etc.)
#     for folder in sorted(os.listdir(root_dir)):
#         folder_path = os.path.join(root_dir, folder)
#         if os.path.isdir(folder_path) and (
#             folder.startswith("2024_") or folder.startswith("2025_")
#         ):
#             # Get gzipped CSV files in the folder, sorted by name
#             gz_files = sorted(
#                 [f for f in os.listdir(folder_path) if f.endswith(".csv.gz")]
#             )
#             for gz_file in gz_files:
#                 file_path = os.path.join(folder_path, gz_file)
#                 print(f"Processing {file_path}...")
#                 with gzip.open(file_path, "rb") as fin:
#                     lines = fin.readlines()
#                     if first_chunk:
#                         # Write all lines including the header for the very first file
#                         fout.writelines(lines)
#                         first_chunk = False
#                     else:
#                         # Skip the first line (header) and write the rest
#                         fout.writelines(lines[1:])

# print("Combined CSV created at:", combined_file_path)


import pandas as pd
import os
import re


def sanitize_filename(filename):
    # Remove or replace characters that are not allowed in filenames
    sanitized = re.sub(r'[<>:"/\\|?*]', "_", filename)
    return sanitized.strip()


def export_excel_sheets_to_csv():
    # Use raw string for file paths
    excel_file_path = r"D:\Work\Full-time\Uptimal\Test case\NYC_311_Data\datainfo.xlsx"
    output_dir = r"D:\Work\Full-time\Uptimal\Test case\NYC_311_Data"

    # Read the Excel file
    xls = pd.ExcelFile(excel_file_path)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through each sheet and export to CSV
    for sheet_name in xls.sheet_names:
        # Read the sheet
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

        # Sanitize sheet name for filename
        safe_sheet_name = sanitize_filename(sheet_name)

        # Create CSV filename using the sanitized sheet name
        csv_filename = os.path.join(output_dir, f"{safe_sheet_name}.csv")

        # Export to CSV
        df.to_csv(csv_filename, index=False)
        print(f"Exported {sheet_name} to {csv_filename}")


# Run the export
export_excel_sheets_to_csv()
