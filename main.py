  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)