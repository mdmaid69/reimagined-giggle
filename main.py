  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)