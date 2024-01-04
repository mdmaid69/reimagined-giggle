  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)