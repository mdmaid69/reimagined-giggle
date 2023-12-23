  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()