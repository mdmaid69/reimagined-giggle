  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)