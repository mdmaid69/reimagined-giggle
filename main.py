  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time