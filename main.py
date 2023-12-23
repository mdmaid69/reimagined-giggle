  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
def is_palindrome(s):
        return s == s[::-1]