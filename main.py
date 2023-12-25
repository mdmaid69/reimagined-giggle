import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks