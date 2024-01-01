  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)