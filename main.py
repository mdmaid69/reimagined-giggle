  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)