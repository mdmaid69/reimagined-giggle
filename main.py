import math
def calculate_logarithm(base, x):
        return math.log(x, base)
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns