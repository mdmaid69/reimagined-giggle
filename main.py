  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)