  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)