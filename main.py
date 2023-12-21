  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)