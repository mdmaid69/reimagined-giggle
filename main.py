  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)