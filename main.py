  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)