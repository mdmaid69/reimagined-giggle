  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()