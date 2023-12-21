import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)