  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time