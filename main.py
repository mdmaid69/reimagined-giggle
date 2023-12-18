  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())