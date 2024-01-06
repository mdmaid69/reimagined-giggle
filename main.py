import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)