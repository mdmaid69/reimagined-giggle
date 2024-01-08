  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)