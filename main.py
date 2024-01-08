import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)