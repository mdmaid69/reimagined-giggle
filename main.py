  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))