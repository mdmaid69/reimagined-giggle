  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))