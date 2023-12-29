  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a