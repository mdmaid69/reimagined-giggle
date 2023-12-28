  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a