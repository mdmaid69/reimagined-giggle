  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))