  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height