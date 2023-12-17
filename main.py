  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)