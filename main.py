import os
def remove_directory(path):
        os.rmdir(path)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))