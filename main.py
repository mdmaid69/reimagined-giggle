import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)