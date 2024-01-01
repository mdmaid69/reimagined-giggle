  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)