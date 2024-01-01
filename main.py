  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)