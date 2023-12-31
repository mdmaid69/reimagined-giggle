  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)