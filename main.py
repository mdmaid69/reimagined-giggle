  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)