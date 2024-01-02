import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)