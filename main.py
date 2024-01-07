  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)