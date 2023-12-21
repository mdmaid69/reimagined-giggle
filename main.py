  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))