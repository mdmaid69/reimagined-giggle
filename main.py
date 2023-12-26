import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)