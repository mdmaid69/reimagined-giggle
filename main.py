  import os
  def split_path(path):
        return os.path.split(path)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)