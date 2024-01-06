  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import math
def calculate_sign(x):
        return math.copysign(1, x)