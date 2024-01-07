  import os
  def delete_file(file_name):
        os.remove(file_name)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)