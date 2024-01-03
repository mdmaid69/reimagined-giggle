  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)