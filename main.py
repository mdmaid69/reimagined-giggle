  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)