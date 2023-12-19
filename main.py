  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)