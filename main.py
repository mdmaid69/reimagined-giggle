  import os
  def get_current_directory():
        return os.getcwd()
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))