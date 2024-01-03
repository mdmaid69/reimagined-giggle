  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import math
def calculate_logarithm_base_2(x):
        return math.log2(x)