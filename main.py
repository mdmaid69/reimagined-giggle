import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)