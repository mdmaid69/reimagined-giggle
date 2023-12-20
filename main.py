  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import math
def calculate_logarithm(base, x):
        return math.log(x, base)