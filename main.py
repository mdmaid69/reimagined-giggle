  import os
  def split_path(path):
        return os.path.split(path)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))