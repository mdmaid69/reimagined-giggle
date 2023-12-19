  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)