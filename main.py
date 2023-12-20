  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)