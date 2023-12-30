  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)