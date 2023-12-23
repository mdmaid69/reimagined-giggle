import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))