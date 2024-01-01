  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)