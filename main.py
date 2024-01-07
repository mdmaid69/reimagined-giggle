import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)