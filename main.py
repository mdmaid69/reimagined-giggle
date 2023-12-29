import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)