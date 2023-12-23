  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a