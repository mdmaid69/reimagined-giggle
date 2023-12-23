  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)