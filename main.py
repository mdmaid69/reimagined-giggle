  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)