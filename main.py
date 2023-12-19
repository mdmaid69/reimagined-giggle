  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)