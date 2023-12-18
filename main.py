  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)