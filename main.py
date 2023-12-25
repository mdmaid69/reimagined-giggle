  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)