# remove duplicate from global HC file
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import os

# hide root
root = tk.Tk()
root.withdraw()

# Open File picker for CSV
file_path = filedialog.askopenfilename(
    title="Select CSV File",
    filetypes=[("CSV files", "*csv")]
)

# Load CSV if a file was selected
if file_path:
    main_df = pd.read_csv(file_path, encoding="Latin1")
    print(f"Load file: {file_path}")
else:
    print("No file selected.")

col_to_merge = ["Source File", "Employee ID", "Country"]
main_df["Merged1"] =(
    main_df[col_to_merge]
    .fillna("Unknown")
    .astype(str)
    .agg("".join, axis=1)
)
main_df = main_df.drop_duplicates(subset="Merged1")
main_df = main_df.drop(columns=["Merged1"])

main_df.to_csv(file_path, index=False, encoding="utf-8-sig")

print(f"file exported")
# %%
