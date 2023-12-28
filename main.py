  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())