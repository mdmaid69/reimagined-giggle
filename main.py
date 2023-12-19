  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)