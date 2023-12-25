def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)