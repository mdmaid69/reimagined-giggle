  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)