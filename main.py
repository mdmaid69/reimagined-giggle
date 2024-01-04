  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)