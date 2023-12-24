  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)