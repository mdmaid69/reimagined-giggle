  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a