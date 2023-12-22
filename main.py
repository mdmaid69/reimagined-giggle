  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)