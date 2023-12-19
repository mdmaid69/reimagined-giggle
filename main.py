  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)