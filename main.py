  import os
  def delete_file(file_name):
        os.remove(file_name)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)