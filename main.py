import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize