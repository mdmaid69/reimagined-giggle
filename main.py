import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)