  import os
  def get_base_name(path):
        return os.path.basename(path)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)