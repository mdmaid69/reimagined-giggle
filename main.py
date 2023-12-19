import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))