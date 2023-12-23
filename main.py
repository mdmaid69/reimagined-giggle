  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)