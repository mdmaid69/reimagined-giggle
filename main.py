  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))