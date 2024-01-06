import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)