  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)