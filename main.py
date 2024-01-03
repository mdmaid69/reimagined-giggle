  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))