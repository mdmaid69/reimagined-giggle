import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize