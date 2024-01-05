import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)