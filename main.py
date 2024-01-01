import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)