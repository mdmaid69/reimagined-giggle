import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)