  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)