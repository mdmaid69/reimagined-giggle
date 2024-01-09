  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a