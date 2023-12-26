import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)