  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import re
def split_string(pattern, string):
        return re.split(pattern, string)