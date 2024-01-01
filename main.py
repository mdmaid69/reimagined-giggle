  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)