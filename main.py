  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]