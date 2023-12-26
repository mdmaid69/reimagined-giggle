import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)