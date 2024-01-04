  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))