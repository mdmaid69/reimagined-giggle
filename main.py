  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)