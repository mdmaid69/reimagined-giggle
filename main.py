  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)