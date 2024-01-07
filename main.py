  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)