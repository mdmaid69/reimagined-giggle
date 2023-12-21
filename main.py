  import numpy as np
  def calculate_median(arr):
        return np.median(arr)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()