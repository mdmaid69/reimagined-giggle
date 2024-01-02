def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)