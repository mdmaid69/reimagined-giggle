  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}