  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)