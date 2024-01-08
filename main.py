  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
def calculate_roi(gain, cost):
        return (gain - cost) / cost