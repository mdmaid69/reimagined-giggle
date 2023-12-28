  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)