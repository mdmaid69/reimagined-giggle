  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)