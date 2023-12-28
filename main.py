  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time