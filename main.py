  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)