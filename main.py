  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a