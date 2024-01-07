  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import sys
def add_to_python_path(path):
        sys.path.append(path)