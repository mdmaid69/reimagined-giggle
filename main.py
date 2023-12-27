  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)