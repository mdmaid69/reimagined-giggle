  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius