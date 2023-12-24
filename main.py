  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)