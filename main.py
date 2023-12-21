import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)