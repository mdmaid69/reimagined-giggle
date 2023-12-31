  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)