  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)