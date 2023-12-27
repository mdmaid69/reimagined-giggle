import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)