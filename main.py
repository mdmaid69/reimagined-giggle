import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)