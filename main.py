import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)