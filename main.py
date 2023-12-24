  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable