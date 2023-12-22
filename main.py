  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)