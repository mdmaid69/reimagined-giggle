  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)