  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()