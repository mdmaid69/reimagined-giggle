  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import math
def calculate_remainder(x, y):
        return math.remainder(x, y)