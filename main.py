import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)