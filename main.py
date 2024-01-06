import math
def calculate_logarithm(base, x):
        return math.log(x, base)
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize