  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)