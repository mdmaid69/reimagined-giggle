  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)