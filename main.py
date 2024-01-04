  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)