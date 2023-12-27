  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)