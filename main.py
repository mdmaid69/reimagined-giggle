import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)