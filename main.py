  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)