import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)