  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()