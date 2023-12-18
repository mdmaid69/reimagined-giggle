  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import platform
def get_os_info():
        return platform.uname()