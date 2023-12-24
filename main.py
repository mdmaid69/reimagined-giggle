  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))