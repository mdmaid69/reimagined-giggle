  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value