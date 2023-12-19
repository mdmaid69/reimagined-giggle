  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)