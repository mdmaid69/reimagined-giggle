  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)