  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)