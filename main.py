import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)