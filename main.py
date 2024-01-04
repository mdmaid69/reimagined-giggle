import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)