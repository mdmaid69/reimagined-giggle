import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))