  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)