import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)