  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)