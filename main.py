  import os
  def get_current_working_directory():
        return os.getcwd()
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)