  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a