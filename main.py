import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)