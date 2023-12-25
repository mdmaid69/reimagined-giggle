  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)