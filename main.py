  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)