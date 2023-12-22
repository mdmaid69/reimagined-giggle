  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)