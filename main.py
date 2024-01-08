  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a