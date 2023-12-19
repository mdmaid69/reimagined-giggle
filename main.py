  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time