  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)