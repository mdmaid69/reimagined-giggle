  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))