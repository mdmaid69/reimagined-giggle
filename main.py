  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)