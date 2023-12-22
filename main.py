  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)