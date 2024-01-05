  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a