  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)