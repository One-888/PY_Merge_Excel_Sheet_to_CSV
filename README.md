# PY_Merge_Excel_Sheet_to_CSV
Merge all excel files into one csv file

Usage:

from merge_all_excel_sheet_to_csv import main


main(
    selected_columns='"Account Number","Premise","Service Address","Meter Number","Doc Amount in $","Usage in TGals","Billing Date","Due Date","Rate Category"',
    file_name="CY*.xlsx",
    file_prefix="CY",
    file_extension=".xlsx",
    top_rows=10,
    output_file="output",
)
