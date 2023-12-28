import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)