  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)