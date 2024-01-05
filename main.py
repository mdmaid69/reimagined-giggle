import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)