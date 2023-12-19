  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()