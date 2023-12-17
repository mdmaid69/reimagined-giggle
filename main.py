  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)