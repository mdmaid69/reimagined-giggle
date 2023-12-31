import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)