  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)