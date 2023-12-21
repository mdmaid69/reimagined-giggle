  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)