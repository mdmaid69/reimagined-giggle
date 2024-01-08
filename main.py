  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
  import os
  def get_base_name(path):
        return os.path.basename(path)