  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))