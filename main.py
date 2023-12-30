  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)