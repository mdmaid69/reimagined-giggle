  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)