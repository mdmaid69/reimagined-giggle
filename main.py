  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time