  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))