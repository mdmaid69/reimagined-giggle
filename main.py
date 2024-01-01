  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
def is_palindrome(s):
        return s == s[::-1]