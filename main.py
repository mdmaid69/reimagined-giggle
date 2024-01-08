def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)