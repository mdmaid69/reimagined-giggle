  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))