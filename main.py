  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)