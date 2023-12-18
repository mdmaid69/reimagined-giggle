  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)