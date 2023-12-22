  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import os
def list_files_in_directory(path):
        return os.listdir(path)