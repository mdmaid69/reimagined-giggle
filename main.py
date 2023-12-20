  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())