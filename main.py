import os
def get_environment_variable(var):
        return os.getenv(var)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))