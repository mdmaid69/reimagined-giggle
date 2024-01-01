  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)