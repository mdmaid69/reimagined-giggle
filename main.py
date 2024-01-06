import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)