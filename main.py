import math
def calculate_exponential(x):
        return math.exp(x)
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns