  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)