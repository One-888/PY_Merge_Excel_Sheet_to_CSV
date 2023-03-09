import pandas as pd
import glob
import csv


def main(
    selected_columns, file_name, file_prefix, file_extension, top_rows, output_file
):
    print(f"Starting..")
    dfs = []

    selected_columns = selected_columns.replace('"', "").split(",")
    print("Selected Cols: ")
    print(selected_columns)
    print()

    for i, x in enumerate(glob.glob(file_name, recursive=False)):  # **/
        print(f"Read file {i:02d}: {x}")
        df = pd.read_excel(x, sheet_name=0, usecols=selected_columns, nrows=top_rows)
        # add cycle
        df["File_Name"] = x.replace(file_prefix, "").replace(file_extension, "")
        df.drop_duplicates()
        dfs.append(df)

    concat_df = pd.concat(dfs)
    concat_df = concat_df.drop_duplicates()

    output_filename = output_file

    # make csv
    print()
    print(f"Merging into one {output_filename}.csv")
    concat_df.to_csv(
        (output_filename + ".csv"),
        index=None,
        header=True,
        sep=";",
        quoting=csv.QUOTE_NONE,
        escapechar="/",
    )
    print()
    print(f"Success!")


if __name__ == "__main__":
    pass
