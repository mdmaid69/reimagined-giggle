  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a