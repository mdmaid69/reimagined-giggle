  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a