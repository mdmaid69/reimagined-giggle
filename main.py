  import os
  def get_base_name(path):
        return os.path.basename(path)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)