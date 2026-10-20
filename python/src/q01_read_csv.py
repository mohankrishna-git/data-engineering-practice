# Question 1: Read all four CSV files using Python and print their row counts and column names.

import csv
from pathlib import Path

# Folder containing the CSV files
data_folder = Path("data/raw")

# Names of the four CSV files
files = [
    "customers.csv",
    "products.csv",
    "orders.csv",
    "order_items.csv"
]

# Read each CSV file
for filename in files:

    file_path = data_folder / filename

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:

        reader = csv.DictReader(file)

        columns = reader.fieldnames
        rows = list(reader)

    print("\nFile:", filename)
    print("Column names:", columns)
    print("Total rows:", len(rows))