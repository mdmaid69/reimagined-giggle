  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value