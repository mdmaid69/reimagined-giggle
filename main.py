def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)