  import math
  def calculate_square_root(n):
        return math.sqrt(n)
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize