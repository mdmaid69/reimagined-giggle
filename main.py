  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]