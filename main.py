  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)