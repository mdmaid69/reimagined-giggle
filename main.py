  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a