  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)