  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)