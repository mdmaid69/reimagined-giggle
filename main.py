import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))