  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height