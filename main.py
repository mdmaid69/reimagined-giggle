  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)