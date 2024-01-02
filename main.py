import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)