import glob
def find_files(pattern):
        return glob.glob(pattern)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)