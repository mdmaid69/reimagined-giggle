import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value