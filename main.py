import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)