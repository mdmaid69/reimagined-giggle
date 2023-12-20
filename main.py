import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)