import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)