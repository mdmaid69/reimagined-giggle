import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))