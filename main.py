  import os
  def get_base_name(path):
        return os.path.basename(path)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)