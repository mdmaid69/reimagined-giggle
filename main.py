  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))