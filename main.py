  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)