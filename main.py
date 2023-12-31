  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)