  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)