  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a