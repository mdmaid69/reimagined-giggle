  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
def calculate_roi(gain, cost):
        return (gain - cost) / cost