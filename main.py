  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)