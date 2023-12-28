import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize