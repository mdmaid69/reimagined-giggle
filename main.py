  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))