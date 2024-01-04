  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))