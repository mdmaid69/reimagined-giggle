  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)