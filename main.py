import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)