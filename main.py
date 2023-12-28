  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)