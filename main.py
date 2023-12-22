  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))