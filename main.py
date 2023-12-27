  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)